# Generated by Django 5.2 on 2025-05-10 00:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_comment"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Comment",
            new_name="omment",
        ),
    ]
