# Generated by Django 5.1.3 on 2024-12-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0002_tguser_tg_auth_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tguser',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='password'),
        ),
    ]
