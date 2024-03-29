import os
import requests
import json
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.core.files.base import ContentFile
from django.views.generic import FormView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, reverse, render
from . import models as user_models
from . import forms as user_forms
from .mixins import LogedOutOnlyMixin
from core import models as core_models


class LoginView(LogedOutOnlyMixin, FormView):

    template_name = "users/login.html"
    form_class = user_forms.UserLoginForm
    
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    # def get_initial(self):
    #     self.initial["email"] = self.kwargs["email"]
    #     return self.initial.copy()


class SignUpView(LogedOutOnlyMixin, FormView):

    template_name = "users/signup.html"
    form_class = user_forms.UserSignUpForm

    success_url = reverse_lazy("users:login")


def logout_view(request):
    logout(request)
    return redirect(reverse("core:intro"))


def kakao_login(request):

    app_key = os.environ.get("KAKAO_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback/"

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
        else:  # error가 없다면
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
            print(kakao_account)
            profile = kakao_account.get("profile")
            email = kakao_account.get("email")
            # gender = kakao_account.get("gender")
            profile_image = profile.get("profile_image-url")

            if email is None:
                raise KakaoException()
            else:  # email 정보를 받아 왓을때
                try:
                    existed_user = user_models.User.objects.get(email=email)
                    print("sdjflskdfjskldfjklsdjfklsjflksjflksjflksflk")
                    if existed_user.login_method == "kakao":
                        login(request, existed_user)
                        if existed_user.is_first:
                            return redirect(reverse("users:fst_edit"))
                        return redirect(reverse("core:home"))
                    else:  # user가 다른방법으로 회원가입 한 경우 통합할지의 여부를 결정
                        return render(request, "intro.html", {"is_duplicate": True})
                except user_models.User.DoesNotExist:
                    new_user = user_models.User.objects.create_user(
                        username=email, email=email, login_method="kakao"
                    )
                    new_user.save()
                    if profile_image is not None:
                        photo_request = requests.get(profile_image)
                        new_user.avatar.save(
                            f"{email}-avatar.png", ContentFile(photo_request.content)
                        )
                    login(request, new_user)
                    return redirect(reverse("users:fst_edit"))

            # try:
            #     user = user_models.User.objects.get(email=email)
            #     if user is not None:
            #         login(request, user)
            #         if not user.is_first:
            #             return redirect(reverse("core:home"))
            #         else:
            #             return redirect(
            #                 reverse("users:fst_edit", kwargs={"alias": user.alias})
            #             )
            # except user_models.User.DoesNotExist:
            #     new_user = user_models.User.objects.create(
            #         username=email, email=email, alias=alias, gender=gender
            #     )

            #     if profile_image is not None:
            #         photo_request = requests.get(profile_image)
            #         new_user.avatar.save(
            #             f"{alias}-avatar", ContentFile(photo_request.content)
            #         )

            #     login(request, new_user)
            #     if new_user.positions.count() == 0:
            #         return redirect(
            #             reverse("users:fst_edit", kwargs={"alias": new_user.alias})
            #         )
            #     else:
            #         return redirect(reverse("core:home"))
    except KakaoException:
        return redirect(reverse("core:home"))


def google_login(request):

    client_id = os.environ.get("GOOGLE_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/google/callback/"
    scopes = "https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile"
    return redirect(
        f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scopes}"
    )


class GoogleException(Exception):

    pass


def google_callback(request):

    try:
        code = request.GET.get("code")
        client_id = os.environ.get("GOOGLE_ID")
        client_secret = os.environ.get("GOOGLE_SECRET")
        grant_type = "authorization_code"
        redirect_uri = "http://127.0.0.1:8000/users/login/google/callback/"

        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "grant_type": grant_type,
            "redirect_uri": redirect_uri,
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        token_response = requests.post(
            "https://oauth2.googleapis.com/token", data=data, headers=headers
        )
        token_json = token_response.json()
        access_token = token_json.get("access_token")

        profile_response = requests.get(
            f"https://www.googleapis.com/oauth2/v1/userinfo?access_token={access_token}"
        )
        profile_json = profile_response.json()
        print(profile_json)
        login_email = profile_json.get("email")
        login_first_name = profile_json.get("given_name")
        login_last_name = profile_json.get("family_name")
        login_avatar = profile_json.get("picture")

        try:
            existed_user = user_models.User.objects.get(email=login_email)

            if existed_user.login_method == "google":
                login(request, existed_user)
                print(existed_user.is_first)
                if existed_user.is_first:
                    return redirect(reverse("users:fst_edit"))
                else:
                    return redirect(reverse("core:home"))
            else:
                raise GoogleException()
        except user_models.User.DoesNotExist:
            user = user_models.User.objects.create_user(
                username=login_email,
                email=login_email,
                first_name=login_first_name,
                last_name=login_last_name,
                email_varified=True,
                login_method="google",
            )
            user.set_unusable_password()
            user.save()
            if login_avatar is not None:
                photo_request = requests.get(login_avatar)
                user.avatar.save(
                    f"{user.email}-avatar.png", ContentFile(photo_request.content)
                )

            login(request, user)
            return redirect(reverse("users:fst_edit"))
    except GoogleException:
        return redirect(reverse("core:intro"))


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


@login_required
def first_edit(request):

    if request.method == "GET":
        login_user = user_models.User.objects.get(email=request.user)
        print(login_user.avatar)
        form = user_forms.MusicianAliasForm(
            {"alias": login_user.alias, "avatar": login_user.avatar, "is_first": True}
        )
        return render(request, "users/fst_edit_alias.html", {"form": form})
    else:
        user = user_models.User.objects.get(email=request.user)
        form = user_forms.MusicianInfoForm(request.POST, request.FILES, instance=user)
        for error in form.errors:
            print(f"error: {error}")
        if form.is_valid():
            print(form.cleaned_data["is_first"])
            form.save()
            return redirect(reverse("users:fst_edit_region"))
        else:
            return render(request, "users/fst_edit_alias.html", {"form": form})


@login_required(redirect_field_name=None)
def first_edit_region(request):

    ACTIVE_REGION = {
        "서울특별시": (
            "종로구",
            "중구",
            "용산구",
            "성동구",
            "광진구",
            "동대문구",
            "중랑구",
            "성북구",
            "강북구",
            "도봉구",
            "노원구",
            "은평구",
            "서대문구",
            "마포구",
            "양천구",
            "강서구",
            "구로구",
            "금천구",
            "영등포구",
            "동작구",
            "관악구",
            "서초구",
            "강남구",
            "송파구",
            "강동구",
        ),
        "부산광역시": (
            "중구",
            "서구",
            "동구",
            "영도구",
            "부산진구",
            "동래구",
            "남구",
            "북구",
            "강서구",
            "해운대구",
            "사하구",
            "금정구",
            "연제구",
            "수영구",
            "사상구",
            "기장군",
        ),
        "대구광역시": ("중구", "동구", "서구", "남구", "북구", "수성구", "달서구", "달성군"),
        "인천광역시": ("중구", "동구", "미주홀구", "연수구", "남동구", "부평구", "계양구", "서구", "강화군", "옹진군"),
        "광주광역시": ("동구", "서구", "남구", "북구", "광산구"),
        "대전광역시": ("동구", "중구", "서구", "유성구", "대덕구"),
        "울산광역시": ("중구", "남구", "동구", "북구", "울주군"),
        "세종특별자치시": ("세종시"),
    }

    user_email = request.user
    cities = ACTIVE_REGION.keys
    boroughs = ACTIVE_REGION.values
    region = json.dumps(ACTIVE_REGION, ensure_ascii=False)
    print(request.method)
    if request.method == "GET":
        login_user = get_object_or_404(user_models.User, email=user_email)
        form = user_forms.MusicianActiveRegionForm()
        return render(
            request,
            "users/fst_edit_region.html",
            {"form": form, "region": region, "cities": cities, "boroughs": boroughs},
        )
    else:
        login_user = get_object_or_404(user_models.User, email=user_email)
        form = user_forms.MusicianInfoForm(
            request.POST, request.FILES, instance=login_user
        )
        print(f"POST data: {request.POST}")
        print(f"File: {request.FILES}")
        if form.is_valid():
            print(f"borough {form.cleaned_data}")
            form.save()
            return redirect(reverse("users:fst_edit_position"), kwargs={"form": form})
        else:
            print(form.errors)
            return render(
                request,
                "users/fst_edit_region.html",
                {
                    "form": form,
                    "region": region,
                    "cities": cities,
                    "boroughs": boroughs,
                },
            )


@login_required(redirect_field_name=None)
def first_edit_position(request):
    positions = core_models.Position.objects.all()

    if request.method == "GET":
        login_user = get_object_or_404(user_models.User, email=request.user)
        form = user_forms.MusicianInfoForm(instance=login_user)
        return render(
            request,
            "users/fst_edit_position.html",
            {"form": form, "positions": positions},
        )
    else:
        login_user = get_object_or_404(user_models.User, email=request.user)
        form = user_forms.MusicianInfoForm(
            request.POST, request.FILES, instance=login_user
        )

        if form.is_valid():
            form.save()
            return redirect(reverse("users:fst_edit_genre"), kwargs={"form": form})
        else:
            return render(
                request,
                "users/fst_edit_position.html",
                {"form": form, "positions": positions},
            )


@login_required(redirect_field_name=None)
def first_edit_genre(request):
    genres = core_models.Genre.objects.all()

    if request.method == "GET":
        login_user = get_object_or_404(user_models.User, email=request.user)
        form = user_forms.MusicianInfoForm(instance=login_user)
        return render(
            request, "users/fst_edit_genre.html", {"form": form, "genres": genres},
        )
    else:
        login_user = get_object_or_404(user_models.User, email=request.user)
        form = user_forms.MusicianInfoForm(
            request.POST, request.FILES, instance=login_user
        )
        if form.is_valid():
            form.save()
            return redirect(reverse("core:home"))
        else:
            return render(
                request, "users/fst_edit_genre.html", {"form": form, "genres": genres}
            )
