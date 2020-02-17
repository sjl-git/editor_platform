from django.urls import path
from . import views

app_name = "suggestions"

urlpatterns = [
    path(
        "<int:proposer_pk>/<int:other_side_pk>/application/<int:application_pk>/",
        views.SuggestionCreateView.as_view(),
        name="create",
    ),
    path("<int:pk>/detail", views.SuggestionDetailView.as_view(), name="detail"),
    path(
        "<int:answerer_pk>/<int:recepient_pk>/suggestion/<int:suggestion_pk>/",
        views.CreateAnswerView.as_view(),
        name="create_answer",
    ),
]
