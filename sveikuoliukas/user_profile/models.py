from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from PIL import Image
import os


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    picture = models.ImageField(_("picture"), upload_to='user_pictures/', blank=True, null=True)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("user_detail_current", kwargs={"pk": self.pk})
    

class Chat(models.Model):
    title = models.CharField(_("name of the chat"), max_length=70, db_index=True)
    description = models.TextField(_("description"), blank=True, max_length=10000)
    image = models.ImageField(_("image"), upload_to='chat_images/', blank=True, null=True)
    owner = models.ForeignKey(
        get_user_model(),
        verbose_name=_("owner"),
        on_delete=models.CASCADE,
        related_name="my_chats",
        null=True
    )
    participants = models.ManyToManyField(
        get_user_model(),
        verbose_name=_("participants"),
        related_name="chats",
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True, null=True)
    is_private = models.BooleanField(_("private chat"), default=False)
        
    class Meta:
        verbose_name = _("chat")
        verbose_name_plural = _("chats")
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("chat_detail", kwargs={"pk": self.pk})
