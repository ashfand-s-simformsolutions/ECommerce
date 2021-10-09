from django.contrib.auth.views import LoginView
from django.shortcuts import resolve_url


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
