from .env import (
    ENVIRONMENT,
    EnvironmentType
)

if ENVIRONMENT == EnvironmentType.DEV:
    BASE_URL: str = "http://localhost:8000/base/api"
else:
    BASE_URL: str = "https://fulcrum-backend-base.onrender.com/base/api"


__all__ = [
    "ENVIRONMENT",
    "EnvironmentType",
    "BASE_URL"
]