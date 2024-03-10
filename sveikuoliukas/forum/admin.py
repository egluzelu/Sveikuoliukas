from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'created_at']
    list_display_links = ['name', 'owner']
    list_filter = ['owner']
    search_fields = ['name', 'description', 'owner__last_name', 'owner__username']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (_("general").title(), {
            "fields": (
                'name',
                'owner',
                'description',
            ),
        }),
        (_("temporal tracking").title(), {
            "fields": (
                ('created_at', 'updated_at'),
            ),
        }),
    )


admin.site.register(models.Post, PostAdmin)