from django.urls import path, include
from . import views as core_views


app_name = "core"

urlpatterns = [
    path("", core_views.intro_view, name="intro"),
    path("home/", core_views.home_view, name="home"),
]
