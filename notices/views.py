from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, FormView, View
from . import models, forms
from users import models as user_models


class HomeView(View):
    def get(self, request):
        sample = models.Notice.objects.all()[:4]
        return render(request, "notices/home.html", {"sample": sample})


class NoticeListView(ListView):
    model = models.Notice
    paginate_by = 8
    ordering = "deadline"
    # paginate_orphans = 4
    context_object_name = "notices"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = forms.SearchForm()
        context["form"] = form
        return context

    def get_queryset(self):
        youtube_name = self.request.GET.get("youtube_name")
        if youtube_name is None:
            form = forms.SearchForm(self.request.GET)
            if form.is_valid():
                genre = form.cleaned_data.get("genre")
                print(genre)
            if genre is None:
                qs = super().get_queryset()
                return qs
            else:
                filter_args = {}
                for g in genre:
                    filter_args["genre"] = g
                qs = models.Notice.objects.filter(**filter_args).order_by("-created")
                return qs

        else:
            youtuber = user_models.User.objects.get_or_none(youtube_name=youtube_name)
            if youtuber is None:
                return super().get_queryset().order_by("-created")
            else:
                qs = models.Notice.objects.filter(employer=youtuber)
                return qs


class NoticeCreateView(FormView):
    model = models.Notice
    template_name = "notices/notice_create.html"
    form_class = forms.CreateNoticeForm

    def form_valid(self, form):
        notice = form.save()
        video = form.cleaned_data.get("video")
        employer = self.request.user
        notice.employer = employer
        notice.save()
        form.save_m2m()
        models.NoticeVideo.objects.create(video=video, notice=notice)
        return redirect(reverse("core:home"))


class NoticeDetailView(DetailView):
    model = models.Notice


@login_required
def delete_notice(request, pk):
    user = request.user
    try:
        notices = models.Notice.objects.get(pk=pk)
        if notices.employer == user:
            notices.delete()
        next_arg = request.GET.get("next")
        if next_arg is not None:
            return redirect(next_arg)
        else:
            return redirect(reverse("core:home"))
    except models.Notice.DoesNotExist:
        return redirect(reverse("core:home"))
