from django.conf import settings
from django.shortcuts import render

BOT_NAME = settings.BOT_NAME
AUTH_URL = settings.AUTH_URL


def auth(request):
    return render(
        request,
        'auth.html',
        context={
            'bot_name': BOT_NAME,
            'auth_url': AUTH_URL,
        }
    )
