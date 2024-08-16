# tests/test_helloworld.py
import pytest
from django.test import Client


@pytest.mark.django_db
def test_helloworld_page(client: Client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.content == b"Hello, World!"
