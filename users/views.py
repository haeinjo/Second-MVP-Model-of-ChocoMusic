import os
import requests
from django.core.files.base import ContentFile
from django.contrib.auth import login
from django.shortcuts import redirect, reverse, render
from . import models as user_models
from . import forms as user_forms


def kakao_login(request):

    app_key = os.environ.get("KAKAO_ID")
    redirect_uri = f"http://127.0.0.1:8000/users/login/kakao/callback/"

    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_key}&redirect_uri={redirect_uri}&response_type=code"
    )


class KakaoException(Exception):

    pass


def kakao_callback(request):

    try:
        error = request.GET.get("error")

        if error is not None:
            raise KakaoException()
        else:
            grant_type = "authorization_code"
            client_id = os.environ.get("KAKAO_ID")
            redirect_uri = f"http://127.0.0.1:8000/users/login/kakao/callback/"
            code = request.GET.get("code")

            data = {
                "grant_type": grant_type,
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "code": code,
            }
            headers = {
                "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
            }

            token_request = requests.post(
                f"https://kauth.kakao.com/oauth/token", data=data, headers=headers
            )
            token_json = token_request.json()

            access_token = token_json.get("access_token")
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
            }
            profile_request = requests.post(
                f"https://kapi.kakao.com/v2/user/me", headers=headers
            )
            profile_json = profile_request.json()

            kakao_account = profile_json.get("kakao_account")
            profile = kakao_account.get("profile")
            email = kakao_account.get("email")
            gender = kakao_account.get("gender")
            profile_image = profile.get("profile_image-url")
            alias = profile.get("nickname")

            if email is None:
                raise KakaoException()

            try:
                user = user_models.User.objects.get(email=email)
                if user is not None:
                    login(request, user)
                    print(type(user.positions.count()))
                    if user.positions.count() != 0:
                        return redirect(reverse("core:home"))
                    else:
                        return redirect(
                            reverse("users:fst_edit", kwargs={"alias": user.alias})
                        )
            except user_models.User.DoesNotExist:
                new_user = user_models.User.objects.create(
                    username=email, email=email, alias=alias, gender=gender
                )

                if profile_image is not None:
                    photo_request = requests.get(profile_image)
                    new_user.avatar.save(
                        f"{alias}-avatar", ContentFile(photo_request.content)
                    )

                login(request, new_user)
                if new_user.positions.count() == 0:
                    return redirect(
                        reverse("users:fst_edit", kwargs={"alias": new_user.alias})
                    )
                else:
                    return redirect(reverse("core:home"))
    except KakaoException:
        return redirect(reverse("core:home"))


def naver_login(request):

    client_id = os.environ.get("NAVER_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/naver/callback/"
    state = os.environ.get("NAVER_STATE")
    return redirect(
        f"https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&state={state}"
    )


class NaverException(Exception):

    pass


def naver_callback(request):

    try:
        grant_type = "authorization_code"
        client_id = os.environ.get("NAVER_ID")
        client_secret = os.environ.get("NAVER_SECRET")
        code = request.GET.get("code")
        state = os.environ.get("NAVER_STATE")

        data = {
            "grant_type": grant_type,
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "state": state,
        }

        token_request = requests.post("https://nid.naver.com/oauth2.0/token", data=data)
        token_json = token_request.json()

        access_token = token_json.get("access_token")
        headers = {"Authorization": f"Bearer {access_token}"}
        naver_request = requests.post(
            "https://openapi.naver.com/v1/nid/me", headers=headers
        )
        naver_json = naver_request.json()
        print(naver_json)
    except NaverException():
        pass


def first_edit(request, alias):

    if request.method == "GET":
        form = user_forms.MusicianInfoForm(request.GET)
        return render(request, "users/fst_edit.html", {"form": form})
    else:
        user = user_models.User.objects.get(alias=alias)
        form = user_forms.MusicianInfoForm(request.POST, instance=user)
        form.save()
        return redirect(reverse("core:home"))
