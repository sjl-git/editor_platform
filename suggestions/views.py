from django.shortcuts import redirect
from django.urls import reverse
from django.http import Http404
from django.views.generic import View, DetailView
from . import models
from users import models as user_models
from applications import models as application_models


class SuggestionCreateView(View):
    def post(self, *args, **kwargs):
        application_pk = kwargs.get("application_pk")
        cost = self.request.POST.get("cost", None)
        proposer_pk = kwargs.get("proposer_pk")
        other_side_pk = kwargs.get("other_side_pk")
        application = application_models.Application.objects.get_or_none(
            pk=application_pk
        )
        proposer = user_models.User.objects.get_or_none(pk=proposer_pk)
        other_side = user_models.User.objects.get_or_none(pk=other_side_pk)
        if proposer is None or other_side is None or application is None:
            raise Http404()
        else:
            suggestion = models.Suggestion.objects.get_or_none(
                proposer=proposer, other_side=other_side, application=application
            )
            if suggestion is None:
                models.Suggestion.objects.create(
                    proposer=proposer,
                    other_side=other_side,
                    cost=cost,
                    application=application,
                )
            else:
                suggestion.cost = cost
                suggestion.has_answer = False
                suggestion.save()
            notice_pk = application.notice.pk
            return redirect(reverse("notices:detail", kwargs={"pk": notice_pk}))


class SuggestionDetailView(DetailView):
    model = models.Suggestion


class CreateAnswerView(View):
    def post(self, *args, **kwargs):
        result = self.request.GET.get("accept")
        answerer_pk = kwargs.get("answerer_pk")
        recepient_pk = kwargs.get("recepient_pk")
        suggestion_pk = kwargs.get("suggestion_pk")
        answerer = user_models.User.objects.get(pk=answerer_pk)
        recepient = user_models.User.objects.get(pk=recepient_pk)
        suggestion = models.Suggestion.objects.get(pk=suggestion_pk)
        if answerer is None and recepient is None and suggestion is None:
            raise Http404
        else:
            answer = models.Answer.objects.get_or_none(
                answerer=answerer, recepient=recepient, suggestion=suggestion
            )
            if answer is None:
                if result:
                    models.Answer.objects.create(
                        answerer=answerer,
                        recepient=recepient,
                        suggestion=suggestion,
                        answer=result,
                    )
                    suggestion.has_answer = True
                    suggestion.save()
                else:
                    models.Answer.obejects.create(
                        answerer=answerer,
                        recepient=recepient,
                        suggestion=suggestion,
                        answer=result,
                    )
                    suggestion.has_answer = True
                    suggestion.save()
            return redirect(reverse("users:profile"))
