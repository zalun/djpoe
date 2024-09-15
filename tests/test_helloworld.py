# tests/test_helloworld.py
import pytest
from django.test import Client


@pytest.mark.django_db
def test_helloworld_page(client: Client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Hello, World!" in response.content.decode()


@pytest.mark.django_db
def test_homepage_unauthenticated(client: Client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Welcome, guest!" in response.content.decode()
    assert "Login" in response.content.decode()
    assert "Sign Up" in response.content.decode()
    assert "Logout" not in response.content.decode()


@pytest.mark.django_db
def test_homepage_authenticated(client: Client, username: str, password: str):
    client.login(username=username, password=password)

    response = client.get("/")

    assert response.status_code == 200
    assert f"Welcome, {username}!" in response.content.decode()
    assert "Logout" in response.content.decode()
    assert "Login" not in response.content.decode()
    assert "Sign Up" not in response.content.decode()
