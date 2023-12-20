import pytest
from check_post import get_login
import yaml


@pytest.fixture()
def token():
    return get_login()




