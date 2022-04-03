from typing import Dict, Any
from exception.proxy_error import ProxyRequestError, ProxyHttpStatusError
import httpx


class HttpClientWrapper:
    def post(self, url: str, body: Dict[str, Any]):
        with httpx.Client() as client:
            try:
                r = client.post(url=url, json=body)
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
