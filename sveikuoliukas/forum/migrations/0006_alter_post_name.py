# Generated by Django 5.0 on 2024-03-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, max_length=70, verbose_name='name of the post'),
        ),
    ]