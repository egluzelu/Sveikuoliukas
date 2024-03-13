# Generated by Django 5.0 on 2024-03-12 16:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0013_remove_chat_receiver_owner_chat_receiver_owner'),
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
            field=models.ManyToManyField(related_name='my_send_messages', to=settings.AUTH_USER_MODEL, verbose_name='receiver_owner'),
        ),
    ]