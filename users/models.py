from datetime import date
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.html import mark_safe
from django.db import models
from core import managers


class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    youtube_name = models.CharField(max_length=80, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    objects = managers.CustomUserManager()

    def get_thumbnail(self):
        if self.avatar.name != "":
            return mark_safe(f"<img width='100px' src = '{ self.avatar.url }' /img>")
        else:
            return None

    def get_avatar(self):
        return self.avatar.url

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def get_age(self):
        today = date.today()
        k_age = today.year - self.birthdate.year + 1
        return k_age

    def count_unanswered_suggestions_and_answers(self):
        result = 0
        for suggestion in self.received_suggestions.all():
            if suggestion.has_answer is False:
                result = result + 1
        for answer in self.received_answers.all():
            result = result + 1
        return result
