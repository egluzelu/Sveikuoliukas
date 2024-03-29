# Generated by Django 5.0 on 2024-03-12 08:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_chat_delete_message'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='sender',
        ),
        migrations.AddField(
            model_name='chat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chat_images/', verbose_name='image'),
        ),
        migrations.AddField(
            model_name='chat',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='private chat'),
        ),
        migrations.AddField(
            model_name='chat',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chats', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
    ]
