from django.urls import path
from .views import TgAuthAPIView

urlpatterns = [
    path('telegram-auth/', TgAuthAPIView.as_view(), name='telegram-auth'),
]
