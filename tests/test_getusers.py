import pytest
from utils.baseclass import BaseClass

@pytest.fixture(scope="module")
def obj():
  return BaseClass()

def test_getusers_validation(obj):
  response = obj.get("users")
  print(response.json())
  assert response.status_code == 200
  assert len(response.json()) > 0
  assert response.elapsed.total_seconds() < 1
