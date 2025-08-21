import pytest
from utils.baseclass import BaseClass

@pytest.fixture(scope="class")
def create_users_obj():
  return BaseClass()

def test_getusers_validation(create_users_obj):
  response = create_users_obj.get("users")
  print(response.json())
  assert response.status_code == 200
  assert len(response.json()) > 0
  assert response.elapsed.total_seconds() < 2
