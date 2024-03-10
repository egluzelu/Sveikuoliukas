from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from PIL import Image
import os


class Comment(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        verbose_name=_("owner"),
        on_delete=models.CASCADE,
        related_name="comments",
    )
    post = models.ForeignKey(
        'Post',
        verbose_name=_("post"),
        on_delete=models.CASCADE,
        related_name="comments",
    )
    description = models.TextField(_("description"), blank=True, max_length=10000)
    image = models.ImageField(_("image"), upload_to='comment_images/', blank=True, null=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True, null=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, db_index=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
        ordering = ['-created_at']


class Post(models.Model):
    name = models.CharField(_("name of the post"), max_length=70, db_index=True)
    description = models.TextField(_("description"), blank=True, max_length=10000)
    image = models.ImageField(_("image"), upload_to='post_images/', blank=True, null=True)
    owner = models.ForeignKey(
        get_user_model(),
        verbose_name=_("owner"),
        on_delete=models.CASCADE,
        related_name="posts",
    )

    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True, null=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, db_index=True, null=True)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
