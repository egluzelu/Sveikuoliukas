from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Board(models.Model):
    name = models.CharField(_("name of the Board"), max_length=100, db_index=True)
    description = models.TextField(_("description"), blank=True, max_length=100000)
    owner = models.ForeignKey(
        get_user_model(),
        verbose_name=_("owner"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("board")
        verbose_name_plural = _("board")
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("board_detail", kwargs={"pk": self.pk})
    