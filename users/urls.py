from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("profile", views.UserProfileView.as_view(), name="profile"),
    path("update-profile", views.UpdateProfileView.as_view(), name="update"),
    path("change-password", views.ChangePasswordView.as_view(), name="password"),
]
