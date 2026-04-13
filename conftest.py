import pytest
from client import ReqResClient

@pytest.fixture
def api_client():
    return ReqResClient()
