from django.contrib import admin

from ..models import TgUser


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    pass
