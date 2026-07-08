import ssl

from .certs import RUSSIAN_TRUSTED_CA

__all__ = ["create_ssl_context"]


def create_ssl_context(trust_russian_ca: bool = True) -> ssl.SSLContext:
    context = ssl.create_default_context()
    if trust_russian_ca:
        context.load_verify_locations(cafile=str(RUSSIAN_TRUSTED_CA))
    return context
