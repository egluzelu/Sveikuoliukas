# Generated by Django 5.0 on 2024-03-18 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board_main', '0003_remove_board_image_remove_board_sub_title_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Board',
        ),
    ]