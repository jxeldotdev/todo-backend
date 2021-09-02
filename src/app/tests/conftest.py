from typing import Generator
from app.database import SessionLocal
import pytest


@pytest.fixture(scope="module")
def db() -> Generator:
    yield SessionLocal()


# @pytest.fixture(scope="module", autouse=True)
# def cfg() -> Settings:
#     Settings()
