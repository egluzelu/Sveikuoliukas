# Generated by Django 5.0 on 2024-03-12 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_main', '0002_alter_board_options_remove_board_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='image',
        ),
        migrations.RemoveField(
            model_name='board',
            name='sub_title',
        ),
        migrations.AddField(
            model_name='board',
            name='description',
            field=models.CharField(blank=True, db_index=True, max_length=100, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=100, verbose_name='title'),
        ),
    ]
