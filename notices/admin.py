from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.NoticeVideo)
class NoticeVideoAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
