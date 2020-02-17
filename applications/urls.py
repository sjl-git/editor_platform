from django.urls import path
from . import views

app_name = "applications"

urlpatterns = [
    path("<int:pk>/apply/", views.UploadApplicationView.as_view(), name="apply"),
    path("<int:pk>/delete/", views.delete_application, name="delete",),
    path("<int:pk>/detail/", views.ApplicationDetailView.as_view(), name="detail"),
]
