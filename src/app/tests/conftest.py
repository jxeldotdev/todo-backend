from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app import database

from app.database import SessionLocal
from app.main import app, TodoAppConfig


@pytest.fixture(scope="module")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def cfg():
    with TodoAppConfig() as cfg:
        yield cfg
    

@pytest.fixture(autouse=True, scope="function")
def teardown(db: Session) -> None:
    db.execute("TRUNCATE TABLE {}".format(database.DB_NAME))
    

    