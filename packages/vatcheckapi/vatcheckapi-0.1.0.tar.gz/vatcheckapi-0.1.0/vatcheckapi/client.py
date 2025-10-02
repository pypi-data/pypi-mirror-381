from __future__ import annotations

from typing import Any, Dict, Optional

import requests


DEFAULT_BASE_URL = "https://vatcheckapi.com/api"


class Client:
    """Minimal VAT Check API client.

    Supports authentication via `apikey` header (default) or query parameter.
    Exposes two endpoints: `status` and `validate`.
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        auth_in_query: bool = False,
        header_name: str = "apikey",
        timeout: Optional[float] = 10.0,
        session: Optional[requests.Session] = None,
        default_headers: Optional[Dict[str, str]] = None,
    ) -> None:
        if not api_key:
            raise ValueError("api_key is required")
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.auth_in_query = bool(auth_in_query)
        self.header_name = header_name
        self.timeout = timeout
        self.session = session or requests.Session()
        self.default_headers = {"Accept": "application/json"}
        if default_headers:
            self.default_headers.update(default_headers)

    def _request(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        params = dict(params or {})
        headers = dict(self.default_headers)

        if self.auth_in_query:
            params.setdefault("apikey", self.api_key)
        else:
            headers[self.header_name] = self.api_key

        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = self.session.get(url, params=params, headers=headers, timeout=self.timeout)

        content_type = resp.headers.get("content-type", "")
        is_json = "application/json" in content_type
        data: Any
        if is_json:
            data = resp.json()
        else:
            data = {"raw": resp.text}

        if not resp.ok:
            message = data.get("message") if isinstance(data, dict) else None
            raise requests.HTTPError(
                f"vatcheckapi error: {resp.status_code} {resp.reason}: {message}",
                response=resp,
            )

        if isinstance(data, dict):
            return data
        return {"data": data}

    def status(self) -> Dict[str, Any]:
        """Retrieve API status and quota information."""
        return self._request("status")

    def validate(self, *, vat_number: Optional[str] = None, **params: Any) -> Dict[str, Any]:
        """Validate a VAT number.

        Pass parameters according to the docs, e.g. `vat_number="DE123456789"`.
        Additional keyword arguments are forwarded as query parameters.
        """
        if vat_number is not None:
            params.setdefault("vat_number", vat_number)
        return self._request("validate", params=params)


