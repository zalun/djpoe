# tests/test_admin_page.py
import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_render_admin_login(client: Client):
    url = reverse("admin:login")

    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_redirect_if_not_superuseer(client: Client, django_user_model: User):
    user = django_user_model.objects.create_user("john", password="pass1234")
    client.force_login(user)
    url = reverse("admin:index")

    response = client.get(url)

    assert response.status_code == 302
    assert response.content == b""
    assert response.url == "/admin/login/?next=/admin/"  # type: ignore[attr-defined]


@pytest.mark.django_db
def test_admin_success_for_superuser(client: Client, django_user_model: User):
    user = django_user_model.objects.create_user("john", password="pass1234", is_superuser=True, is_staff=True)
    client.force_login(user)
    url = reverse("admin:index")

    response = client.get(url)

    assert response.status_code == 200
    assert b"Django site admin" in response.content
