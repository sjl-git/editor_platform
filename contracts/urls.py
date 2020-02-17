from django.urls import path
from . import views

app_name = "contracts"

urlpatterns = [
    path(
        "<int:employer_pk>/<int:editor_pk>/application/<int:application_pk>/",
        views.create_contract,
        name="create",
    ),
    path("list/", views.ContractListView.as_view(), name="list"),
    path("message/<int:pk>/delete/", views.delete_message, name="delete_message"),
]
