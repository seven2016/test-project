import pytest
import json
from client import ReqResClient

def load_data():
    with open("testdata.json") as f:
        return json.load(f)

@pytest.fixture
def client():
    return ReqResClient()

@pytest.mark.parametrize("email,password,expected", [
    ("eve.holt@reqres.in", "cityslicka", 200),
    ("eve.holt@reqres.in", "", 400),
])
def test_login_fixture(client, email, password, expected):
    res = client.login(email, password)
    assert res.status_code == expected