from django.urls import path
from notices import views as notice_views

app_name = "core"

urlpatterns = [
    path("", notice_views.HomeView.as_view(), name="home"),
]
