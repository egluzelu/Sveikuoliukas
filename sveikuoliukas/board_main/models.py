from django.db import models
from django.utils.translation import gettext_lazy as _


class Board(models.Model):
    title = models.CharField(_("title"), max_length=100, db_index=True, blank=True)
    description = models.CharField(_("description"), max_length=100, db_index=True, blank=True)
   
    def __str__(self):
        return self.title
