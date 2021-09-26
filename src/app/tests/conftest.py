from collections.abc import Generator

import pytest
from app.database import SessionLocal


@pytest.fixture(scope="module")
def db() -> Generator:
    yield SessionLocal()


# @pytest.fixture(scope="module", autouse=True)
# def cfg() -> Settings:
#     Settings()
