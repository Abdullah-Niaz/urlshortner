from django.urls import path
from . import views

app_name = "shortener"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("<slug:slug>/", views.redirect_view, name="redirect"),
]
