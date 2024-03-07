from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models

class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
    list_display_links = ['name', 'owner']
    list_filter = ['owner']
    search_fields = ['name']
    fieldsets = (
        (None, {
            "fields": (
                'name', 'owner',
                'description',
            ),
        }),
    )
    

admin.site.register(models.Board, BoardAdmin)


