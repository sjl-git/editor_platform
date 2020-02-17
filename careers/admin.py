from django.contrib import admin
from . import models


@admin.register(models.Career)
class CareerAdmin(admin.ModelAdmin):
    pass
