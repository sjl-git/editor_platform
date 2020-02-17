from django.contrib import admin
from . import models


@admin.register(models.Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
