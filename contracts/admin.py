from django.contrib import admin
from . import models


@admin.register(models.Contract)
class ContractAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass
