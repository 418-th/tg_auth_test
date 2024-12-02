import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from rest_framework.request import Request
from unittest.mock import MagicMock, patch
from ..views import TgAuthAPIView
import json

User = get_user_model()

@pytest.fixture
def user(db):
    return User.objects.create(username='testuser', tg_auth_token='test-token', tg_id=12345)

@pytest.fixture
def tg_auth_view():
    return TgAuthAPIView()

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.fixture
def encrypted_token(tg_auth_view):
    return tg_auth_view.encrypt_token('test-token')

def attach_session_to_request(request):
    middleware = SessionMiddleware(lambda req: None)
    middleware.process_request(request)
    request.session.save()
    return request

def test_encrypt_token(tg_auth_view):
    token = "test-token"
    encrypted = tg_auth_view.encrypt_token(token)
    assert isinstance(encrypted, str)
    assert encrypted != token

def test_decrypt_token(tg_auth_view, encrypted_token):
    decrypted = tg_auth_view.decrypt_token(encrypted_token)
    assert decrypted == "test-token"
