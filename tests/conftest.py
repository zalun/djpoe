import pytest


@pytest.fixture(name="username")
def username_fixture():
    return "testuser"


@pytest.fixture(name="password")
def password_fixture():
    return "12345"
