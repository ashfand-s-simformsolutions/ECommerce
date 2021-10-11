from django.urls import path
from django.urls.conf import re_path
from store.views import HomeView, Store


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('store/<int:pk>/', Store.as_view(), name='store'),
]
