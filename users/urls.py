from django.urls import path
from . import views as user_views


app_name = "users"

urlpatterns = [
    path("login/kakao/", user_views.kakao_login, name="kakao_login"),
    path("login/kakao/callback/", user_views.kakao_callback, name="kakao_callback"),
    path("fst_edit/", user_views.first_edit, name="fst_edit"),
    path("fst_edit_region/", user_views.first_edit_region, name="fst_edit_region"),
    path("fst_edit_positon/", user_views.first_edit_position, name="fst_edit_position"),
    path("fst_edit_genre/", user_views.first_edit_genre, name="fst_edit_genre"),
    path("login/naver/", user_views.naver_login, name="naver_login"),
    path("login/naver/callback/", user_views.naver_callback, name="naver_callback"),
    path("login/google/", user_views.google_login, name="google_login"),
    path("login/google/callback/", user_views.google_callback, name="google_callback"),
]
