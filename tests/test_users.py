import pytest
from utils.baseclass import BaseClass

@pytest.fixture(scope="module")
def obj():
  return BaseClass()

def test_get_users(obj):
  response = obj.get("users")
  # print(response.json())
  assert response.status_code == 200
  assert len(response.json()) > 0
  assert response.elapsed.total_seconds() < 1

def test_create_user(obj):
    user_data = {
        "name": "king",
        "username": "developer",
        "email": "king123@gmail.com"
    }
    response = obj.post("users", user_data)
    # print(response.json())
    assert response.status_code == 201
    assert response.elapsed.total_seconds() < 1
    assert response.json()["name"] == "king"
