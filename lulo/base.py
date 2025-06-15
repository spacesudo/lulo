import requests
from .exceptions import LuloFIError
from typing import Optional

class BaseClient:
    def __init__(self, api_key: str, base_url: str):
        self.session = requests.Session()
        self.session.headers.update({
            "x-api-key": api_key,
            "Content-Type": "application/json"
        })
        self.base_url = base_url

    def _post(self, endpoint: str, data: dict, params: Optional[dict] = None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data, params=params)
        if response.ok:
            return response.json()
        try:
            err_data = response.json()
        except Exception:
            err_data = {}
        raise LuloFIError(
            status_code=response.status_code,
            message=err_data.get("message", "API Request failed"),
            details=err_data.get("details", response.text)
        )

    def _get(self, endpoint: str, params: Optional[dict] = None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        if response.ok:
            return response.json()
        try:
            err_data = response.json()
        except Exception:
            err_data = {}
        raise LuloFIError(
            status_code=response.status_code,
            message=err_data.get("message", "API Request failed"),
            details=err_data.get("details", response.text)
        )