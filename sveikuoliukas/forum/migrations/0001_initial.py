# Generated by Django 5.0 on 2024-03-09 09:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='name of the post')),
                ('description', models.TextField(blank=True, max_length=10000, verbose_name='description')),
                ('image', models.ImageField(null=True, upload_to='post_images', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='updated at')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=10000, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='updated at')),
                ('image', models.ImageField(null=True, upload_to='post_images', verbose_name='image')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.post', verbose_name='post')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ['-created_at'],
            },
        ),
    ]
