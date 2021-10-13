from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import RegisterView, LoginView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
]
