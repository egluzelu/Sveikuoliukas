# Generated by Django 5.0 on 2024-03-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_alter_comment_image_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, max_length=700, verbose_name='name of the post'),
        ),
    ]