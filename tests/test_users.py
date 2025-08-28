import pytest
from utils.baseclass import BaseClass
from conftest import user_details

@pytest.fixture(scope="module")
def obj():
  return BaseClass()

def test_get_users(obj):
  response = obj.get("users")
  # print(response.json())
  assert response.status_code == 200
  assert len(response.json()) > 0
  assert response.elapsed.total_seconds() < 1

@pytest.mark.parametrize("user_data", user_details)
def test_create_user(obj, user_data):
    response = obj.post("users", user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.elapsed.total_seconds() < 1
    assert response.json()["name"] == user_data["name"]
    id = response.json()["id"]
    get_response = obj.get(f"users/{id}")
    get_response = obj.get(f"users/10")
    print(get_response .json())
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Clementina DuBuque"

def test_update_user(obj, load_test_data):
    # user_data = {
    #     "name": "ajay",
    #     "username": "developer",
    #     "email": "prince123@gmail.com"
    # }
    user_data = load_test_data["update_user_details"]
    response = obj.put("users/1", user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1
    assert response.json()["name"] == "Subha"

def test_delete_user(obj):
  response = obj.delete("users/1")
  print(response.json())
  assert response.status_code == 200
  assert len(response.json()) == 0
  assert response.elapsed.total_seconds() < 1
