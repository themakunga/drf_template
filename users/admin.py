
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import UserModel

@admin.register (UserModel)
class UserAdmin(admin.ModelAdmin):
    """User admin."""

    list_display = ('pk', 'email',)
    list_display_links = ('pk', 'email',)

    search_fields = (
        'email',
        'username',
        'first_name',
        'last_name',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'date_joined',
        'updated_at',
    )

    readonly_fields = ('date_joined', 'created_at', 'updated_at')
