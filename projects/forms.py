from django import forms
from . import models


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ("name",)

    def save(self, *args, **kwargs):
        project = super().save(commit=False)
        return project
