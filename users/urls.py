from django.urls import path
from . import views as user_views


app_name = "users"

urlpatterns = [
    path("", user_views.kakao_login, name="kakao_login"),
    path("login/kakao/callback/", user_views.kakao_callback, name="kakao_callback"),
]