# Generated by Django 5.0.1 on 2024-01-28 11:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserProfile',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='buyGeoloy',
            new_name='buyGeology',
        ),
    ]