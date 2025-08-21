from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


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

    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('role',)}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('role',)}),
    # )
    # search_fields = ('username', 'email')
    # ordering = ('username',)
    # filter_horizontal = ()
    # def get_queryset(self, request):
    #     """
    #     Override to ensure that the queryset includes the role field.
    #     """
    #     qs = super().get_queryset(request)
    #     return qs.select_related('role')
    # def save_model(self, request, obj, form, change):
    #     """
    #     Override to handle any custom save logic if needed.
    #     """
    #     super().save_model(request, obj, form, change)
    #     # Additional save logic can be added here if necessary
    # def delete_model(self, request, obj):
    #     """
    #     Override to handle any custom delete logic if needed.
    #     """
    #     super().delete_model(request, obj)
    #     # Additional delete logic can be added here if necessary
