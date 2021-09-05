import logging

from typing import List
from os import getenv

logger = logging.getLogger(__name__)


class RequiredSettingMissingException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{__class__}: {self.message}"


class Settings:
    def getSetting(self, key, default=None):
        """
        Return a setting from an environment variable
        """

        env_key = str(key).upper()
        try:
            val = getenv(env_key).strip("\n")
            if val is not None:
                if "," in val:
                    return val.split(",")
                return val
            else:
                logger.error(f"Environment variable {env_key} not present")
                return default
        except EnvironmentError as e:
            logger.error(e)
            logger.error(f"Environment variable {env_key} not present")

            if default:
                return default

    @property
    def allowed_origins(self) -> List[str]:
        """
        Return allowed origins for CORS settings
        """
        origins = self.getSetting("cors_allowed_origins", [])
        if len(origins) == 0:
            logger.error(
                "Environment variable CORS_ALLOWED_ORIGINS not present.")
            raise RequiredSettingMissingException(
                "CORS Settings missing. CORS_ALLOWED_ORIGINS not present."
            )
        logger.debug(f"Returning CORS Origins from settings - {origins}")
        return origins

    @property
    def database_url(self) -> str:
        """
        Constructs database URL from environment variables
        """
        db_url = (
            "postgresql://POSTGRES_USER:POSTGRES_PASSWORD@POSTGRES_HOST/POSTGRES_DB"  # noqa: E501
        )
        db_vars = ["POSTGRES_USER", "POSTGRES_PASSWORD",
                   "POSTGRES_HOST", "POSTGRES_DB"]

        for key in db_vars:
            val = self.getSetting(key)
            if val is None:
                logger.error(
                    f"Unable to construct database url, missing env var {key}")
                raise RequiredSettingMissingException(f"{key} missing")
            else:
                db_url = db_url.replace(key, val)

        return db_url


cfg = Settings()
