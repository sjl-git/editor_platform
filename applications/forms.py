from django import forms
from . import models


class CreateApplicationForm(forms.ModelForm):
    class Meta:
        model = models.Application
        fields = (
            "cost",
            "video",
        )

    def save(self, *args, **kwargs):
        return super().save(commit=False)
