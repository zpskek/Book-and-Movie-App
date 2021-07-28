from django.urls import path
from users import views as user_views

app_name = "users"

urlpatterns = [
    path("signup/", user_views.SignUpView.as_view(), name="signup"),
    path("login/", user_views.LoginView.as_view(), name="login"),
]