# Generated by Django 4.2 on 2024-03-21 17:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userdetail',
            unique_together={('user', 'phone_number')},
        ),
    ]
