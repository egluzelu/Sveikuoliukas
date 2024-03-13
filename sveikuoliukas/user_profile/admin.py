from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _


class ChatAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at']
    list_display_links = ['title', 'owner']
    list_filter = ['owner']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at']
    fieldsets = (
        (_("general").title(), {
            "fields": (
                'title',
                'owner',
                'description',
                'receiver',
            ),
        }),
        (_("temporal tracking").title(), {
            "fields": (
                ('created_at'),
            ),
        }),
    )

admin.site.register(models.Profile)
admin.site.register(models.Chat, ChatAdmin)

