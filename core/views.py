import os
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from users import models as user_models
from contents import models as content_models


def intro_view(request):
    app_key_k = os.environ.get("KAKAO_JS")

    if request.method == "GET":
        return render(request, "intro.html", {"app_key_k": app_key_k})
    else:
        email = request.POST.get("email")
        try:
            user = user_models.User.objects.get(email=email)
            if user.login_method == "eamil":
                return redirect(reverse("users:login", kwargs={"email": email}))
            else:
                login(request, user)
                if user.is_first:
                    return redirect(reverse("users:fst_edit"))
                else:
                    return redirect(reverse("core:home"))
        except user_models.User.DoesNotExist:
            return redirect(reverse("users:signup", kwargs={"email": email}))


@login_required
def home_view(request):
    login_user = request.user

    user = user_models.User.objects.get(email=login_user)
    positions = user.positions.all()
    genres = user.genres.all()

    if request.method == "GET":
        if positions is not None:
            p_songs = []
            for position in positions:
                for genre in genres:
                    songs = content_models.Content.objects.filter(
                        project__team__members__positions=position
                    ).filter(genre=genre)
                    p_songs += list(songs)
            p_songs = p_songs[0:5]

            # categories = playlist_models.ListCategory.objects.all()
            # playlists = {}
            # for category in categories:
            #     if category.used:
            #         playlists[category.title] = playlist_models.PlayList.objects.filter(
            #             category=category
            #         ).only("songs")[:4]

            teams = user.teams.all()

            return render(
                request,
                "users/home.html",
                {
                    "user": user,
                    "p_songs": p_songs,
                    # "playlists": playlists,
                    "teams": teams,
                },
            )

    return render(request, "users/home.html", {"user": user})
