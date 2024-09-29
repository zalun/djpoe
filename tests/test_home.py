# tests/test_home.py

import pytest
from django.core.management import call_command
from django.test import Client


@pytest.mark.django_db
def test_homepage(client: Client):
    call_command("loaddata", "homepage.json")

    response = client.get("/")
    assert "DJPoe - boilerplate for side projects" in response.content.decode()
