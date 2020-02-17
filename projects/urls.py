from django.urls import path
from . import views

app_name = "projects"
urlpatterns = [
    path("<int:pk>/", views.ProjectView.as_view(), name="list"),
    path(
        "<int:pk>/createproject",
        views.ProjectCreateView.as_view(),
        name="create_project",
    ),
    path(
        "<int:pk>/upload/", views.ProjectFileCreateView.as_view(), name="upload_files"
    ),
    path("<int:pk>/detail/", views.ProjectDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", views.delete_project, name="delete_project"),
    path(
        "project_file/<int:pk>/delete/",
        views.delete_project_file,
        name="delete_project_file",
    ),
    path(
        "edited_video/<int:pk>/delete/",
        views.delete_edited_video,
        name="delete_edited_video",
    ),
    path("comment/<int:pk>/delete/", views.delete_comment, name="delete_comment"),
    path(
        "edited_video/<int:edited_video_pk>/confirm/",
        views.ConfirmProjectView.as_view(),
        name="confirm_edited_video",
    ),
]
