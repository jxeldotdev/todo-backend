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
            val = getenv(env_key)
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
                "CORS settings missing. Environment variable CORS_ALLOWED_ORIGINS not present.")
            raise RequiredSettingMissingException(
                "CORS Settings missing. CORS_ALLOWED_ORIGINS not present.")
        logger.debug(f"Returning CORS Origins from settings - {origins}")
        return origins

    @property
    def database_url(self) -> str:
        """
        Constructs database URL from environment variables
        """
        db_url = "postgresql://POSTGRES_USER:POSTGRES_PASSWORD@POSTGRES_HOST/POSTGRES_DB"
        l = [
            "POSTGRES_USER",
            "POSTGRES_PASSWORD",
            "POSTGRES_HOST",
            "POSTGRES_DB"]

        for key in l:
            val = self.getSetting(key)
            if val is None:
                logger.error(
                    f"Unable to construct database url, missing env var {key}")
                raise RequiredSettingMissingException(f"{key} missing")
            else:
                db_url = db_url.replace(key, val)

        return db_url

    @property
    def jwt_secret_key(self) -> str:
        """
        Returns secret key for jwt
        """
        val = self.getSetting("jwt_secret_key")
        if not val:
            raise RequiredSettingMissingException("JWT Secret key not set.")
        return val

    @property
    def jwt_algorithm(self) -> str:
        return self.getSetting("jwt_algorithm", "HS256")

    @property
    def jwt_token_expiry(self) -> int:
        """
        Return time in minutes for JWT Token to expire.
        """
        return self.getSetting("jwt_token_expiry", 30)

    @property
    def admin_username(self) -> str:
        return self.getSetting("admin_user", "admin")

    @property
    def admin_password(self) -> str:
        return self.getSetting("admin_pass", "password")


cfg = Settings()
