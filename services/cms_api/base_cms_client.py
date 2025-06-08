from typing import Union
from urllib import parse

import requests

from configs.constans import BASE_API_URL, USERNAME, PASSWORD


class BaseClient:
    def __init__(self):
        self._session = requests.Session()
        self._refresh_token()
        self.jwt_token = self.get_tokens()["jwt"]

    def _refresh_token(self):
        jwt = self.get_tokens()["jwt"]
        self._session.headers["Authorization"] = f"Bearer {jwt}"

    def _send(self, method: str, url: str, headers: dict = None, **kwargs) -> requests.Response:
        response = getattr(self._session, method)(url=url, headers=headers, **kwargs)

        if response.status_code == requests.codes.unauthorized:
            self._refresh_token()
            response = getattr(self._session, method)(url=url, headers=headers, **kwargs)

        return response

    @staticmethod
    def _build_url(endpoint: str):
        return parse.urljoin(BASE_API_URL, endpoint)

    def get(self, endpoint: str):
        return self._send(method="get", url=self._build_url(endpoint))

    def post(self, endpoint: str, params: dict = None, payload: Union[dict, list] = None, headers: dict = None,):
        return self._send(method="post", url=self._build_url(endpoint), params=params, json=payload, headers=headers)

    def put(self, endpoint: str, params: dict = None, payload: Union[dict, list] = None):
        return self._send(method="put", url=self._build_url(endpoint), params=params, json=payload)

    def patch(self, endpoint: str, params: dict = None, payload: Union[dict, list] = None):
        return self._send(method="patch", url=self._build_url(endpoint), params=params, json=payload)

    def delete(self):
        # TODO will be added in case of developer starts use this method
        pass

    def get_tokens(self):
        payload = {"login": USERNAME, "password": PASSWORD}
        response = requests.post(url=self._build_url("authorization/login"), json=payload)
        jwt = response.json()["jwt"]
        refresh_token = response.json()["refreshToken"]
        return {"jwt": jwt, "refresh_token": refresh_token}
