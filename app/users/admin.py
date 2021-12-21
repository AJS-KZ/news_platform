from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_superuser')
    list_filter = ('email', )

    fieldsets = (
        (
            'Main', {
                'fields': ('email', 'password',)
            }
        ),
        (
            'Additional information', {
                'fields': ('first_name', 'last_name', 'avatar', 'kind')
            }
        ),
        (
            'Permissions', {
                'fields': ('is_staff', 'is_active', 'groups',)
            }
        )
    )
    add_fieldsets = (
        (
            'Main', {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'kind',)
            }
        ), (
            'permissions', {
                'fields': ('is_staff', 'is_active', 'groups',)
            }
        )
    )
    search_fields = ('email',)
    ordering = ('email',)
