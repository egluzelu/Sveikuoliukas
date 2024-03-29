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
    sender = models.ForeignKey(
        get_user_model(),
        verbose_name=_("sender"),
        on_delete=models.CASCADE,
        related_name="sent_chats",
        null=True,
    )
    receiver = models.ForeignKey(
        get_user_model(),
        verbose_name=_("receiver"),
        on_delete=models.CASCADE,
        related_name="received_chats",
        null=True,
    )
    title = models.CharField(_("name of the chat"), max_length=25, db_index=True, null=True)
    description = models.TextField(_("description"), blank=True, max_length=10000, null=True)
    image = models.ImageField(_("image"), upload_to='chat_images/', blank=True, null=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True, null=True)
           
    class Meta:
        verbose_name = _("chat")
        verbose_name_plural = _("chats")
        ordering = ['-created_at']

    def __str__(self):
        return "{} {} {}".format(
            self.sender,
            _("sent by"),
            self.receiver,
        )
    
    def get_absolute_url(self):
        return reverse("chat_detail", kwargs={"pk": self.pk})
