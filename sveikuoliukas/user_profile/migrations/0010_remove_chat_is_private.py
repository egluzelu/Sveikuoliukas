# Generated by Django 5.0 on 2024-03-12 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0009_alter_chat_is_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='is_private',
        ),
    ]
