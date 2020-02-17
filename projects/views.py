from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.generic import ListView, View, DeleteView, FormView
from . import models, forms
from contracts import models as contract_models


class ProjectView(View):
    def get(self, request, pk):
        contract_pk = pk
        contract = contract_models.Contract.objects.get_or_none(pk=contract_pk)
        if contract is None:
            raise Http404
        else:
            queryset = models.Project.objects.filter(contract=contract)
            messages = contract.messages.all()
            return render(
                request,
                "projects/project_list.html",
                {"projects": queryset, "contract": contract, "messages": messages},
            )

    def post(self, *args, **kwargs):
        message = self.request.POST.get("message", None)
        pk = kwargs.get("pk")
        contract = contract_models.Contract.objects.get_or_none(pk=pk)
        if not contract:
            raise Http404()
        if message is not None:
            contract_models.Message.objects.create(
                message=message, user=self.request.user, contract=contract
            )
        return redirect(reverse("projects:list", kwargs={"pk": pk}))


class ProjectCreateView(FormView):
    model = models.Project
    template_name = "projects/project_create.html"
    form_class = forms.CreateProjectForm

    def form_valid(self, form):
        project = form.save()
        contract_pk = self.kwargs.get("pk")
        contract = contract_models.Contract.objects.get_or_none(pk=contract_pk)
        if contract is None:
            raise Http404
        else:
            project.contract = contract
            project.save()
            return redirect(reverse("projects:list", kwargs={"pk": contract_pk}))


class ProjectFileCreateView(View):
    def post(self, *args, **kwargs):
        project_pk = kwargs.get("pk")
        file = self.request.FILES.get("upload_file", None)
        project = models.Project.objects.get_or_none(pk=project_pk)
        if project is None:
            raise Http404
        else:
            contract_pk = project.contract.pk
            if file is not None:
                models.ProjectFile.objects.create(source=file, project=project)
            return redirect(reverse("projects:list", kwargs={"pk": contract_pk}))


class ProjectDetailView(View):
    def get(self, *args, **kwargs):
        project_pk = kwargs.get("pk")
        project = models.Project.objects.get_or_none(pk=project_pk)
        if project is None:
            raise Http404
        else:
            edited_videos = project.edited_videos.all()
            project_comments = project.comments.all()
            return render(
                self.request,
                "projects/project_detail.html",
                {
                    "edited_videos": edited_videos,
                    "project_comments": project_comments,
                    "project": project,
                },
            )

    def post(self, *args, **kwargs):
        message = self.request.POST.get("message", None)
        pk = kwargs.get("pk")
        project = models.Project.objects.get_or_none(pk=pk)
        if not project:
            raise Http404()
        if message is not None:
            models.Comment.objects.create(
                comment=message, user=self.request.user, project=project
            )
        return redirect(reverse("projects:detail", kwargs={"pk": pk}))


class ConfirmProjectView(View):
    def get(self, *args, **kwargs):
        edited_video_pk = kwargs.get("edited_video_pk")
        edited_video = models.EditedVideo.objects.get_or_none(pk=edited_video_pk)
        if edited_video is None:
            return redirect(reverse("core:home"))
        else:
            edited_video.confirmed = True
            edited_video.save()
            project = edited_video.project
            project.confirmed = True
            project.save()
            unconfirmed_videos = project.edited_videos.all()
            for unconfirmed_video in unconfirmed_videos:
                if unconfirmed_video.confirmed is False:
                    unconfirmed_video.delete()
            project.save()
            return redirect(reverse("projects:detail", kwargs={"pk": project.pk}))


@login_required
def delete_edited_video(request, pk):
    user = request.user
    try:
        edited_video = models.EditedVideo.objects.get(pk=pk)
        if edited_video.project.contract.editor == user:
            edited_video.delete()
        next_arg = request.GET.get("next")
        if next_arg is not None:
            return redirect(next_arg)
        else:
            return redirect(reverse("core:home"))
    except models.EditedVideo.DoesNotExist:
        return redirect(reverse("core:home"))


@login_required
def delete_comment(request, pk):
    user = request.user
    try:
        comment = models.Comment.objects.get(pk=pk)
        if comment.user == user:
            comment.delete()
        next_arg = request.GET.get("next")
        if next_arg is not None:
            return redirect(next_arg)
        else:
            return redirect(reverse("core:home"))
    except models.Comment.DoesNotExist:
        return redirect(reverse("core:home"))


@login_required
def delete_project(request, pk):
    user = request.user
    try:
        project = models.Project.objects.get(pk=pk)
        if project.contract.employer == user:
            project.delete()
        next_arg = request.GET.get("next")
        if next_arg is not None:
            return redirect(next_arg)
        else:
            return redirect(reverse("core:home"))
    except models.Project.DoesNotExist:
        return redirect(reverse("core:home"))


def delete_project_file(request, pk):
    user = request.user
    try:
        project_file = models.ProjectFile.objects.get(pk=pk)
        if project_file.project.contract.employer == user:
            project_file.delete()
        next_arg = request.GET.get("next")
        if next_arg is not None:
            return redirect(next_arg)
        else:
            return redirect(reverse("core:home"))
    except models.ProjectFile.DoesNotExist:
        return redirect(reverse("core:home"))
