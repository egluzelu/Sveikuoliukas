# Generated by Django 5.0 on 2024-03-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_remove_comment_description_remove_comment_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=10000, verbose_name='body'),
        ),
    ]