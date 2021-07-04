from app.settings import RequiredSettingMissingException
from app.settings import cfg

import os
import pytest

def test_allowed_origins_env() -> None:

    origins = "http://localhost:8080,http://localhost:8000"
    origins_list = origins.split(",")
    os.environ['CORS_ALLOWED_ORIGINS'] = origins
    val = cfg.allowed_origins

    assert val == origins_list
    assert type(val) is list

def test_allowed_origins_no_env() -> None:
    """
    Assert that RequiredSettingMissingException is raised when env var CORS_ALLOWED_ORIGINS is not present or is blank
    """

    os.environ.pop('CORS_ALLOWED_ORIGINS')

    with pytest.raises(RequiredSettingMissingException):
        val = cfg.allowed_origins

        assert len(val) is 0

def test_database_url() -> None:
    os.environ['POSTGRES_USER'] = "user"
    os.environ['POSTGRES_PASSWORD'] = "password"
    os.environ['POSTGRES_HOST'] = "host"
    os.environ['POSTGRES_DB'] = 'database'

    assert cfg.database_url == "postgresql://user:password@host/database"
