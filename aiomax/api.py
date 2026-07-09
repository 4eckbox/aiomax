API_BASE_URL = "https://platform-api2.max.ru"

__all__ = ["API_BASE_URL", "build_api_url"]


def build_api_url(path: str) -> str:
    if not path.startswith("/"):
        path = f"/{path}"
    return f"{API_BASE_URL}{path}"
