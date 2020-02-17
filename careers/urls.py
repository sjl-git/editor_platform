from django.urls import path
from . import views

app_name = "careers"
urlpatterns = [
    path("<int:user_pk>/career/", views.CareerDetailView.as_view(), name="detail"),
]
