import os
from django.core.files.base import ContentFile
from django.shortcuts import redirect
from django.urls import reverse
from django.http import Http404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from . import models
from users import models as user_models
from projects import models as project_models
from applications import models as application_models


@login_required
def create_contract(self, employer_pk, editor_pk, application_pk):
    employer = user_models.User.objects.get_or_none(pk=employer_pk)
    editor = user_models.User.objects.get_or_none(pk=editor_pk)
    application = application_models.Application.objects.get_or_none(pk=application_pk)
    if employer is None or editor is None or application is None:
        raise Http404
    else:
        contract = models.Contract.objects.create(
            employer=employer, editor=editor, cost=application.suggestion.cost
        )
        project = project_models.Project.objects.create(
            name="프로젝트 1", contract=contract, confirmed=True
        )
        edited_video = project_models.EditedVideo.objects.create(
            name="영상 1", video="a", project=project, confirmed=True
        )
        source_attachment = application.video
        filecontent = ContentFile(source_attachment.file.read())
        filename = os.path.split(source_attachment.file.name)[-1]
        edited_video.video.save(filename, filecontent)
        edited_video.save()
        source_attachment.file.close()
        return redirect(reverse("core:home"))


class ContractListView(ListView):
    model = models.Contract
    context_object_name = "contracts"

    def get_queryset(self):
        queryset = models.Contract.objects.filter(employer=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        editor_contracts = models.Contract.objects.filter(editor=self.request.user)
        context["editor_contracts"] = editor_contracts

        return context


@login_required
def delete_message(request, pk):
    user = request.user
    try:
        message = models.Message.objects.get(pk=pk)
        if message.user == user:
            message.delete()
        next_arg = request.GET.get("next")
        if next_arg is not None:
            return redirect(next_arg)
        else:
            return redirect(reverse("core:home"))
    except models.Message.DoesNotExist:
        return redirect(reverse("core:home"))
