from enum import Enum
from decouple import config

class EnvironmentType(str, Enum):
    DEV = "dev"
    PROD = "prod"

ENVIRONMENT: EnvironmentType = config(
    "SOAGVNEYONWADUHRNSCH", 
    default=EnvironmentType.PROD
)
# ENVIRONMENT: EnvironmentType = EnvironmentType.PROD
# print("ENVIRONMENT", ENVIRONMENT)