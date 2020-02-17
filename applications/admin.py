from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass
