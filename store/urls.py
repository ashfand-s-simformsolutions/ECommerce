from django.urls import path
from store.views import HomeView, StoreView, DescriptionView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("store/<int:pk>/", StoreView.as_view(), name="store"),
    path("description/<int:pk>/", DescriptionView.as_view(), name='description'),
]
