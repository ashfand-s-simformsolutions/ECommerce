from django.urls import path
from store.views import HomeView, Store


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('store/<int:pk_test>/', Store.as_view(), name='store'),
]
