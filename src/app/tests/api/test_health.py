# noqa: E501
from fastapi.testclient import TestClient
from app import main
from app.tests.utils import utils
import logging

logger = logging.getLogger(__name__)


def test_health_get():
    """
    Test that /health returns a 200 when it can connect to db
    """

    client = TestClient(main.app)
    utils.recreate()
    response = client.get("/health")
    assert response.status_code == 200

# def test_health_get_fail():
#     """
#     Test that /health returns a 500 when it can't connect to DB
#     """

#     client = TestClient(main.app)
#     old_db_url = cfg.database_url
# noqa: E501  cfg.database_url = "postgresql://POSTGRES_USER:POSTGRES_PASSWORD@POSTGRES_HOST/POSTGRES_DB"
#     response = client.get("/health")
#     assert response.status_code == 500
#     cfg.database_url == old_db_url
