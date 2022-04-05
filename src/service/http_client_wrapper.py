from typing import Dict, Any
from exception.proxy_error import ProxyRequestError, ProxyHttpStatusError
import httpx


class HttpClientWrapper:
    def __init__(self, client: httpx.Client):
        self.client = client

    def close(self):
        self.client.close()

    def post(self, url: str, body: Dict[str, Any]):
        try:
            r = self.client.post(url=url, json=body)
            r.raise_for_status()
        except httpx.RequestError as e:
            raise ProxyRequestError(
                f"Error occured while calling {url}, with body {body}"
            ) from e
        except httpx.HTTPStatusError as e:
            raise ProxyHttpStatusError(
                f"Invalid status code returned from {r.url}, with msg {r.text}"
            ) from e
        return r.json()


class AsyncHttpClientWrapper:
    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def close(self):
        return await self.client.aclose()

    async def post(self, url: str, body: Dict[str, Any]):
        try:
            r = await self.client.post(url=url, json=body)
            r.raise_for_status()
        except httpx.RequestError as e:
            raise ProxyRequestError(
                f"Error occured while calling {url}, with body {body}"
            ) from e
        except httpx.HTTPStatusError as e:
            raise ProxyHttpStatusError(
                f"Invalid status code returned from {r.url}, with msg {r.text}"
            ) from e
        return r.json()
