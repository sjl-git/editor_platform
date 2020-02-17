from django.urls import path
from . import views

app_name = "notices"
urlpatterns = [
    path("", views.NoticeListView.as_view(), name="list"),
    path("<int:pk>", views.NoticeDetailView.as_view(), name="detail"),
    path("<int:pk>/delete", views.delete_notice, name="delete"),
    path("create/", views.NoticeCreateView.as_view(), name="create"),
]
