from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, DetailView
from django.views.generic.edit import BaseDeleteView
from . import models, forms
from notices import models as notice_models
from users import mixins


class UploadApplicationView(mixins.LoggedInOnlyView, FormView):
    model = models.Application
    form_class = forms.CreateApplicationForm
    template_name = "applications/application_create.html"

    def form_valid(self, form):
        application = form.save()
        notice_pk = self.kwargs.get("pk")
        notice = notice_models.Notice.objects.get(pk=notice_pk)
        try:
            models.Application.objects.get(notice=notice, applicant=self.request.user)
        except models.Application.DoesNotExist:
            application.applicant = self.request.user
            application.notice = notice
            application.save()
        return redirect(reverse("notices:detail", kwargs={"pk": notice_pk}))


@login_required
def delete_application(request, pk):
    user = request.user
    try:
        applications = models.Application.objects.get(pk=pk)
        if applications.applicant == user:
            applications.delete()
        next_arg = request.GET.get("next")
        if next_arg is not None:
            return redirect(next_arg)
        else:
            return redirect(reverse("core:home"))
    except models.Application.DoesNotExist:
        return redirect(reverse("core:home"))


class ApplicationDetailView(DetailView):
    model = models.Application
