from typing import Dict, Generator
from fastapi.testclient import TestClient

from app.database import SessionLocal
from app.main import app
from app.models import Todo
from app.settings import Settings

import pytest

@pytest.fixture(scope="module")
def db() -> Generator:
    yield SessionLocal()


# @pytest.fixture(scope="module", autouse=True)
# def cfg() -> Settings:
#     Settings()