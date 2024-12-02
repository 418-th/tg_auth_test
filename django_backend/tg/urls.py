from django.urls import path
from .views import auth, TgAuthAPIView

urlpatterns = [
    path('auth', auth, name='auth'),
    path('telegram-auth/', TgAuthAPIView.as_view(), name='telegram-auth'),
]
