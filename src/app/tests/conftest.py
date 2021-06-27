from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import sql
import sqlalchemy
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.main import app
from app.models import Todo


@pytest.fixture(scope="module")
def db() -> Generator:
    yield SessionLocal()


# @pytest.fixture(scope="module")
# def client() -> Generator:
#     with TestClient(app) as c:
#         yield c

# @pytest.fixture(autouse=True, scope="function")
# def teardown(db: SessionLocal) -> None:
#     db.execute("TRUNCATE TABLE todo")
