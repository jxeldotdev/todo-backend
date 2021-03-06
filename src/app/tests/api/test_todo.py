from fastapi.testclient import TestClient
from app import main
from app.tests.utils import utils

import logging

# from app.tests import helpers


logger = logging.getLogger(__name__)


def test_read_todos_empty():
    """
    Test that /todo returns an empty array when no items exist
    """

    client = TestClient(main.app)
    utils.recreate()
    response = client.get("/todo")
    assert response.json() == {"detail": "Item not found"}


def test_write_todo():
    """
    Test that creating a todo at /todo creates a todo item
    """

    content = {
        "title": "Example todo 123 123",
        "notes": "Example notes",
        "completed": "False",
    }

    client = TestClient(main.app)
    response = client.post("/todo", json=content)

    rsp = response.json()

    assert response.status_code == 201

    assert isinstance(rsp["id"], int)
    assert rsp["title"] == content["title"]
    assert rsp["notes"] == content["notes"]
    assert rsp["completed"] is False


def test_read_todos():
    """
    Create 3 todo items and read them all
    """
    content = {
        "title": "Example todo 1",
        "notes": "Example notes 1",
        "completed": "False",
    }

    utils.recreate()
    client = TestClient(main.app)

    for i in range(0, 3):
        print(i)
        content["title"] = f"Example todo {i}"
        content["notes"] = f"Example notes {i}"
        response = client.post("/todo", json=content)

    response = client.get("/todo")
    rsp = response.json()
    logger.info(rsp)
    assert response.status_code == 200
    assert len(rsp) >= 3

    i = 0
    for item in rsp:
        assert item["title"] == f"Example todo {i}"
        assert item["notes"] == f"Example notes {i}"
        assert item["completed"] is False
        i += 1


def test_update_todo():
    """
    Create a new todo item and update it
    """

    client = TestClient(main.app)

    content = {
        "title": "Example todo 6",
        "notes": "Example notes 6",
        "completed": "False",
    }

    post = client.post("/todo", json=content)

    post_rsp = post.json()

    updated_content = {
        "id": post_rsp["id"],
        "title": "Example todo 7",
        "notes": "Example notes 7",
        "completed": "True",
        "created_at": post_rsp["created_at"]
    }

    path = f"/todo/{post_rsp['id']}"

    put = client.put(path, json=updated_content)

    put_rsp = put.json()
    post_rsp = post.json()

    get_updated = client.get(path)
    get_rsp = get_updated.json()

    assert put.status_code == 200
    assert put_rsp == {}
    assert get_rsp["id"] == post_rsp["id"]
    assert get_rsp["title"] == updated_content["title"]
    assert get_rsp["notes"] == updated_content["notes"]
    assert get_rsp["completed"]


def test_delete_todo():

    client = TestClient(main.app)

    content = {
        "title": "Example todo 6",
        "notes": "Example notes 6",
        "completed": "False",
    }

    post = client.post("/todo", json=content)

    post_rsp = post.json()

    path = f"todo/{post_rsp['id']}"

    delete = client.delete(path)

    rsp = post.json()
    del_rsp = delete.json()
    assert post.status_code == 201

    # Check the inital post request is correct
    assert rsp["id"] is not None
    assert rsp["title"] == content["title"]
    assert rsp["notes"] == content["notes"]
    assert rsp["completed"] is False

    assert del_rsp is None
    assert delete.status_code == 204
