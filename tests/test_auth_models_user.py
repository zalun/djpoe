# tests/test_auth_models_user.py
import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db()
def test_user_create(django_user_model: User):
    django_user_model.objects.create_user("john", password="pass1234")

    assert django_user_model.objects.count() == 1
    user = django_user_model.objects.first()
    assert user is not None
    assert user.username == "john"
    assert user.is_active is True
    assert user.is_staff is False
