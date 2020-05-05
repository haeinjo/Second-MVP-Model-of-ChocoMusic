import os
import requests
from django.shortcuts import redirect, reverse


def kakao_login(request):

    app_key = os.environ.get("KAKAO_ID")
    print(app_key)
    redirect_uri = f"http://127.0.0.1:8000/users/login/kakao/callback/"

    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_key}&redirect_uri={redirect_uri}&response_type=code"
    )


def kakao_callback(request):

    error = request.GET.get("error")

    if error is not None:
        return redirect(reverse("core:home"))
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
        headers = {"Content-type": "application/x-www-form-urlencoded;charset=utf-8"}

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

        print(profile_json)
