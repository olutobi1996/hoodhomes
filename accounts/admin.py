from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_agent', 'is_client')
    list_filter = ('is_staff', 'is_superuser', 'is_agent', 'is_client')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'is_agent', 'is_client')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'is_agent', 'is_client')}),
    )
