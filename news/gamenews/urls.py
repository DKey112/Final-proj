from django.urls import path
from . import views


app_name = "gamenews"

urlpatterns = [
    path("gamenews", views.index, name="home"),
]