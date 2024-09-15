# tests/test_accounts_pages.py
import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_login_page_not_authenticated(client: Client):
    response = client.get(reverse("account_login"))

    assert response.status_code == 200
    assert "third-party" in response.content.decode()
    assert '<a title="Google" href="/accounts/google/login/?process=login">Google</a>' in response.content.decode()
