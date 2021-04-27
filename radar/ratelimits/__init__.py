import requests

from functools import lru_cache

PROXY_API = "https://www.proxy-list.download/api/v1/get?type=https&anon=elite"

@lru_cache()
def fetch_proxies():
    return requests.get(PROXY_API).text.splitlines()