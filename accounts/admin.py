from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Team


admin.site.register(Team)
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for the User model.
    This allows for managing users with additional fields and roles.
    """
    fieldsets = UserAdmin.fieldsets + (
        ("Role Info", {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
