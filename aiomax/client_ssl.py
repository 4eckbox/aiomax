import ssl
from typing import Any

import aiohttp

from .certs import RUSSIAN_TRUSTED_CA

__all__ = ["create_client_session", "create_ssl_context"]


def create_ssl_context(trust_russian_ca: bool = True) -> ssl.SSLContext:
    context = ssl.create_default_context()
    if trust_russian_ca:
        context.load_verify_locations(cafile=str(RUSSIAN_TRUSTED_CA))
    return context


def create_client_session(
    *, trust_russian_ca: bool = True, **kwargs: Any
) -> aiohttp.ClientSession:
    connector = kwargs.pop("connector", None)
    if connector is None:
        connector = aiohttp.TCPConnector(
            ssl=create_ssl_context(trust_russian_ca)
        )
    return aiohttp.ClientSession(connector=connector, **kwargs)
