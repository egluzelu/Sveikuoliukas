from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Board(models.Model):
    image = models.ImageField(_("image"), upload_to='board_images/', blank=True, null=True)
    title = models.CharField(_("name of the image"), max_length=100, db_index=True, blank=True)
    sub_title = models.CharField(_("sub_name of the image"), max_length=100, db_index=True, blank=True)
   
    def __str__(self):
        return self.title
    