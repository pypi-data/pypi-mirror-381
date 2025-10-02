# ============================================
# dsf_api_sdk/client.py (FIXED)
# ============================================
from __future__ import annotations

import json
import time
import logging
from functools import wraps
from typing import Dict, Optional, Union, Any
from urllib.parse import urljoin

import requests

from . import __version__
from .exceptions import ValidationError, LicenseError, APIError
from .models import Config, ValidationResult  # asumiendo que existe en tu SDK

logger = logging.getLogger(__name__)

def retry_on_failure(max_retries: int = 3, delay: float = 1.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.RequestException, APIError) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))
                        logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
            raise last_exception
        return wrapper
    return decorator


class APISDK:
    BASE_URL = "https://dsf-gv7x85cv0-jaime-alexander-jimenezs-projects.vercel.app/"
    ENDPOINT = "api/evaluate"   # ← ajusta según tu deploy
    TIERS = {"community", "professional", "enterprise"}

    # Default validation config for API requests
    DEFAULT_API_CONFIG = {
        "auth_token_present": {"default": True, "weight": 5.0, "criticality": 5.0},
        "auth_token_valid_length": {"default": True, "weight": 5.0, "criticality": 5.0},
        "user_verified": {"default": True, "weight": 5.0, "criticality": 5.0},
        "requests_per_minute": {"default": 30, "weight": 4.0, "criticality": 4.0},
        "token_age_minutes": {"default": 15, "weight": 4.0, "criticality": 3.5},
        "ip_reputation_score": {"default": 75, "weight": 4.0, "criticality": 3.0},
    }

    def __init__(
        self,
        license_key: Optional[str] = None,
        tier: str = "community",
        base_url: Optional[str] = None,
        timeout: int = 30,
        verify_ssl: bool = True,
    ):
        if tier not in self.TIERS:
            raise ValidationError(f"Invalid tier: {self.TIERS}")

        self.license_key = license_key
        self.tier = tier
        self.base_url = (base_url or self.BASE_URL)
        if not self.base_url.endswith("/"):
            self.base_url += "/"
        self.timeout = timeout
        self.verify_ssl = verify_ssl

        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": f"DSF-API-SDK-Python/{__version__}",
        })

        # guarda último config no vacío (para métricas)
        self._last_config: Optional[Dict[str, Any]] = None

        if tier != "community" and license_key:
            self._validate_license()

    def _endpoint(self) -> str:
        return self.ENDPOINT

    def _validate_license(self):
        try:
            response = self._make_request(self._endpoint(), {
                "data": {},
                "config": {"test": {"default": 1, "weight": 1.0}},
                "tier": self.tier,
                "license_key": self.license_key,
            })
            if not response.get("tier"):
                raise LicenseError("License validation failed")
        except APIError as e:
            if e.status_code == 403:
                raise LicenseError(f"Invalid license: {e.message}")
            raise

    @retry_on_failure(max_retries=3)
    def _make_request(self, endpoint: str, data: Dict) -> Dict:
        url = urljoin(self.base_url, endpoint)
        try:
            resp = self.session.post(url, json=data, timeout=self.timeout, verify=self.verify_ssl)
            if resp.status_code == 200:
                try:
                    return resp.json()
                except json.JSONDecodeError:
                    raise APIError("Invalid JSON response from server", status_code=200)

            # intenta extraer mensaje de error
            try:
                err = resp.json()
            except Exception:
                err = {"error": (resp.text or "API error").strip()}

            if resp.status_code == 403:
                raise LicenseError(err.get("error", "License error"))
            raise APIError(err.get("error", "API error"), status_code=resp.status_code)
        except requests.RequestException as e:
            raise APIError(f"Request failed: {e}")

    def validate_request(
        self,
        request_data: Dict[str, Any],
        config: Optional[Union[Dict, Config]] = None,
        custom_confidence: Optional[float] = None,
    ) -> ValidationResult:
        """Validate an API request"""
        if isinstance(config, Config):
            config = config.to_dict()
        if not isinstance(request_data, dict):
            raise ValidationError("Request data must be a dictionary")

        final_config = config or self.DEFAULT_API_CONFIG

        payload = {"data": request_data, "config": final_config, "tier": self.tier}
        if self.license_key:
            payload["license_key"] = self.license_key
        if custom_confidence is not None:
            if not 0.0 <= custom_confidence <= 1.0:
                raise ValidationError("Confidence must be between 0.0 and 1.0")
            payload["confidence_level"] = custom_confidence

        response = self._make_request(self._endpoint(), payload)

        # guarda último config válido para get_metrics()
        if final_config:
            self._last_config = final_config

        return ValidationResult.from_response(response)

    def create_config(self) -> Config:
        """Create custom validation config"""
        return Config()

    def get_default_config(self) -> Dict:
        """Get default API validation config"""
        return self.DEFAULT_API_CONFIG.copy()

    def get_metrics(self, config: Optional[Union[Dict, Config]] = None) -> Optional[Dict]:
        if self.tier == "community":
            return None
        if config is None:
            config = self._last_config
        if isinstance(config, Config):
            config = config.to_dict()
        if not config:
            # evita 400 "Config is required" del backend
            config = self.DEFAULT_API_CONFIG

        response = self._make_request(self._endpoint(), {
            "data": {},
            "config": config,
            "tier": self.tier,
            "license_key": self.license_key,
            "get_metrics": True,
        })
        return response.get("metrics")

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
