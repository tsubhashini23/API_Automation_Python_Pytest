import pytest
from utils.baseclass import BaseClass


@pytest.fixture(scope="module")
def obj():
  return BaseClass()

@pytest.mark.smoke
def test_get_users(obj):
  response = obj.get("users")
  # print(response.json())
  assert response.status_code == 200
  assert len(response.json()) > 0
  assert response.elapsed.total_seconds() < 1

# @pytest.mark.parametrize("user_data", user_details)
@pytest.mark.regression
def test_create_user(obj, user_details):
    response = obj.post("users", user_details)
    print(response.json())
    assert "application/json" in response.headers.get("content-type","")
    assert response.status_code == 201
    assert response.elapsed.total_seconds() < 1
    assert response.json()["name"] == user_details["name"]
    # id = response.json()["id"]
    # get_response = obj.get(f"users/{id}")
    # get_response = obj.get(f"users/10")
    # print(get_response .json())
    # assert get_response.status_code == 200
    # assert get_response.json()["name"] == "Clementina DuBuque"

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
