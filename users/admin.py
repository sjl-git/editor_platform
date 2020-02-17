from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("CustomProfile", {"fields": ("avatar", "youtube_name", "birthdate",)},),
    )
    list_display = (
        "username",
        "get_thumbnail",
    )
