from __future__ import annotations
import os
from typing import Any, Dict, Optional
import httpx

from ._errors import (
    AstruxError, AuthenticationError, NotFoundError,
    RateLimitError, ValidationError, ServerError,
)
from ._version import __version__


_DEFAULT_BASE = "https://astrux.io/api/"


def _raise_for_status(resp: httpx.Response):
    msg: str
    try:
        data = resp.json()
        msg = data.get("detail") or data.get("error") or resp.text
    except Exception:
        msg = resp.text

    if resp.status_code in (400, 422):
        raise ValidationError(msg, status=resp.status_code, payload=resp.json() if resp.headers.get("content-type","").startswith("application/json") else None)
    if resp.status_code == 401:
        raise AuthenticationError(msg or "Unauthorized", status=resp.status_code)
    if resp.status_code == 404:
        raise NotFoundError(msg or "Not found", status=resp.status_code)
    if resp.status_code == 429:
        raise RateLimitError(msg or "Rate limited", status=resp.status_code)
    if resp.status_code >= 500:
        raise ServerError(msg or "Server error", status=resp.status_code)
    if resp.status_code >= 400:
        raise AstruxError(msg or f"HTTP {resp.status_code}", status=resp.status_code)


class _ModelsClient:
    def __init__(self, http: httpx.Client, base_url: str, api_key: str):
        self._http = http
        self._base = base_url.rstrip("/")
        self._api_key = api_key

    def predict(self, *, model: str, input: Dict[str, Any], version: Optional[int] = None) -> Dict[str, Any]:
        """
        Calls POST /v1/predict/{model}?version=...
        Body: {"input": {...}}
        """
        if not model:
            raise ValidationError("`model` is required")
        if not isinstance(input, dict):
            raise ValidationError("`input` must be a dict")

        url = f"{self._base}/predict/{model}"
        params = {}
        if version is not None:
            params["version"] = str(version)

        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
            "User-Agent": f"astrux-py/{__version__}",
        }

        resp = self._http.post(url, headers=headers, params=params, json={"input": input})
        _raise_for_status(resp)
        data = resp.json()

        if isinstance(data, dict) and "class" in data and "class_" not in data:
            data["class_"] = data.pop("class")
        return data


class Astrux:
    """
    High-level client:

      client = Astrux(api_key="sk_...")
      client.models.predict(model="name:v2", input={...}, version=None)
    """

    def __init__(self, api_key: Optional[str] = None, *, timeout: float = 30.0):
        self.api_key = api_key or os.getenv("ASTRUX_API_KEY")
        if not self.api_key:
            raise AuthenticationError("Missing API key. Set `api_key=` or ASTRUX_API_KEY env var.")

        self.base_url = _DEFAULT_BASE.rstrip("/")
        self._http = httpx.Client(timeout=timeout, follow_redirects=True)
        self.models = _ModelsClient(self._http, self.base_url, self.api_key)

    def close(self):
        self._http.close()