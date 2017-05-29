from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):

    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'date_joined',
        'created',
        'modified',
    )
    list_filter = (
        'is_active',
    )
    fieldsets = (
        (None, {'fields': (
            'email',
            'password'
        )}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'date_joined',
        )}),
        ('Permissions', {'fields': (
            'is_active',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
            )
        }),
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
    )
    filter_horizontal = ()
    ordering = ('-created',)
