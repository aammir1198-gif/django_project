from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username',
        'full_name',
        'phone_number',
        'age',
        'is_staff',
    )

    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات اضافی', {
            'fields': ('full_name', 'phone_number', 'age'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('اطلاعات اضافی', {
            'fields': ('full_name', 'phone_number', 'age'),
        }),
    )