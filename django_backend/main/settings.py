import os
import environ

from .base_settings import *

env = environ.Env(DEBUG=(bool, False),)  # set default values and casting
environ.Env.read_env()
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

INSTALLED_APPS += [
    'tg',
    'rest_framework',
]
AUTH_USER_MODEL = 'tg.TgUser'

BOT_NAME = os.getenv('BOT_NAME', '')
AUTH_URL = os.getenv('AUTH_URL', '')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', '')

DATABASES = {
    'default': env.db(),
}
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"
