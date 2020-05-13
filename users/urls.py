from django.urls import path
from . import views as user_views


app_name = "users"

urlpatterns = [
    path("login/kakao/", user_views.kakao_login, name="kakao_login"),
    path("login/kakao/callback/", user_views.kakao_callback, name="kakao_callback"),
    path("<str:alias>/fst_edit/", user_views.first_edit, name="fst_edit"),
    path("login/naver/", user_views.naver_login, name="naver_login"),
    path("login/naver/callback/", user_views.naver_callback, name="naver_callback"),
]
