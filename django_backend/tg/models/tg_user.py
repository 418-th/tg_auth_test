import secrets

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser


class TgUserManager(models.Manager):

    def get_or_create_user(self, data):
        tg_id = data.get('tg_id')
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        user = self.get_queryset().filter(
            Q(tg_id=tg_id) | Q(username=username)
        ).first()

        token = secrets.token_urlsafe(16)

        if user and not user.tg_auth_token:
            user.tg_auth_token = token
            user.save(update_fields=['tg_auth_token'])

        elif not user:
            user = self.create(
                tg_id=tg_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                tg_auth_token=token,
            )
        return user

    def update_user(self, tg_id):
        token = secrets.token_urlsafe(16)
        self.get_queryset().filter(tg_id=tg_id).update(tg_auth_token=token)


class TgUser(AbstractUser):
    objects = TgUserManager()

    tg_id = models.CharField(
        'telegram id', max_length=128,
        unique=True, blank=True, null=True
    )
    tg_auth_token = models.CharField(
        'telegram_auth_token', max_length=128,
        unique=True, blank=True, null=True,
    )
    password = models.CharField(
        'password', max_length=128, blank=True, null=True
    )

    class Meta:
        verbose_name = 'telegram user'
        indexes = [
            models.Index(fields=['tg_id',])
        ]
