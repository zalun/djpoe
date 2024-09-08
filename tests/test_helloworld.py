# tests/test_helloworld.py
import pytest
from django.contrib.auth import get_user_model
from django.test import Client


@pytest.mark.django_db
def test_helloworld_page(client: Client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Hello, World!" in response.content.decode()


User = get_user_model()


@pytest.fixture(name="user")
def user_fixture():
    return User.objects.create_user(username="testuser", password="12345")


@pytest.mark.django_db
def test_homepage_unauthenticated(client: Client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Welcome, guest!" in response.content.decode()
    assert "Login" in response.content.decode()
    assert "Sign Up" in response.content.decode()
    assert "Logout" not in response.content.decode()


@pytest.mark.django_db
def test_homepage_authenticated(client: Client, user):
    client.login(username="testuser", password="12345")

    response = client.get("/")

    assert response.status_code == 200
    assert f"Welcome, {user.username}!" in response.content.decode()
    assert "Logout" in response.content.decode()
    assert "Login" not in response.content.decode()
    assert "Sign Up" not in response.content.decode()
