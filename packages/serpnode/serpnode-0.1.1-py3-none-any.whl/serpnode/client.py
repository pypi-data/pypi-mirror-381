from __future__ import annotations

from typing import Any, Dict, Optional
import requests


DEFAULT_BASE_URL = "https://api.serpnode.com/v1"


class Client:
    """Serpnode API client.

    Supports `apikey` header (default) or query parameter `apikey` auth.
    Exposes the core endpoints: status, search, options, locations.
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        auth_in_query: bool = False,
        timeout: Optional[float] = 30.0,
        default_headers: Optional[Dict[str, str]] = None,
    ) -> None:
        if not api_key or not isinstance(api_key, str):
            raise ValueError("'api_key' is required and must be a non-empty string")

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.auth_in_query = bool(auth_in_query)
        self.timeout = timeout
        self.default_headers = {"Accept": "application/json"}
        if default_headers:
            self.default_headers.update(default_headers)

        self._session = requests.Session()
        self._session.headers.update(self.default_headers)

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        params = dict(params or {})
        if self.auth_in_query:
            params["apikey"] = self.api_key

        url = f"{self.base_url}/{path.lstrip('/')}"
        headers = {}
        if not self.auth_in_query:
            headers["apikey"] = self.api_key

        resp = self._session.get(url, params=params, headers=headers, timeout=self.timeout)
        content_type = resp.headers.get("content-type", "")
        is_json = "application/json" in content_type
        data = resp.json() if is_json else resp.text
        if not resp.ok:
            raise requests.HTTPError(
                f"Serpnode API error: {resp.status_code} {resp.reason}",
                response=resp,
            )
        return data

    def status(self) -> Any:
        return self._get("status")

    def search(self, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._get("search", params)

    def options(self, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._get("options", params)

    def locations(self, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._get("locations", params)


