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
