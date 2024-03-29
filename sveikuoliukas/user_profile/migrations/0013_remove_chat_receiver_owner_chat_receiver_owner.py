# Generated by Django 5.0 on 2024-03-12 16:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0012_alter_chat_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='receiver_owner',
        ),
        migrations.AddField(
            model_name='chat',
            name='receiver_owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_send_messages', to=settings.AUTH_USER_MODEL, verbose_name='receiver_owner'),
        ),
    ]
