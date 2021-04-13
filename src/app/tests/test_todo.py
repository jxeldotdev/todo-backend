from fastapi.testclient import TestClient
from app import main

from app.tests import helpers

client = TestClient(main.app)

def test_read_todos_empty():
    """
    Test that /todo returns an empty array when no items exist
    """
    response = client.get("/todo")
    assert response.status_code == 200
    assert response.json() == {"detail": "Not Found"}


def test_write_todo():
    """
    Test that creating a todo at /todo creates a todo item
    """

    response = client.post(
        "/todo",
        json={
            "title": "Example todo",
            "notes": "Example notes",
            "completed": "false",
        },
    )

    assert response.status_code == 200

    # Verify ID is a valid UUID
    resp_json = response.json()
    todo_id = resp_json.id
    assert helpers.check_uuid(todo_id)

    assert response.json() == {
        "id": todo_id,
        "title": "Example todo",
        "notes": "Example notes",
        "completed": "false",
    }


def test_read_todos():
    """
    Test that /todo returns an array with multiple items when multiple items exist
    """
    pass


def test_read_todo(id):
    pathStr = "/todo/{}".format(id)
    response = client.get("/todo/")
    pass
    


def test_update_todo():
    pass


def test_delete_todo():
    pass

