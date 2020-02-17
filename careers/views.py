from django.shortcuts import render
from django.views.generic import ListView
from . import models
from users import models as user_models


class CareerDetailView(ListView):
    model = models.Career

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_pk = self.kwargs.get("user_pk")
        try:
            user = user_models.User.objects.get(pk=user_pk)
            try:
                careers1 = models.Career.objects.filter(user=user)
                context["applicant_career"] = careers1
            except models.Career.DoesNotExist:
                pass
            try:
                careers2 = models.Career.objects.filter(employer=user)
                context["employer_career"] = careers2
            except models.Career.DoesNotExist:
                pass
        except user_models.User.DoesNotExist:
            pass
        return context
