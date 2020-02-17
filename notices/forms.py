from django import forms
from . import models


class CreateNoticeForm(forms.ModelForm):
    video = forms.FileField()

    class Meta:
        model = models.Notice
        fields = (
            "genre",
            "deadline",
            "edited_length",
        )

    def save(self, *args, **kwargs):
        notice = super().save(commit=False)
        return notice


class SearchForm(forms.Form):
    genre = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
