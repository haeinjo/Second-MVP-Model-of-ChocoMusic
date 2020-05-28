import os
import requests
from django.shortcuts import render, redirect, reverse
from users import models as user_models
from songs import models as song_models
from playlists import models as playlist_models


def intro_view(request):
    app_key_k = os.environ.get("KAKAO_JS")

    return render(request, "intro.html", {"app_key_k": app_key_k})


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
                    songs = song_models.Song.objects.filter(
                        roles__position=position
                    ).filter(genre=genre)
                    p_songs += list(songs)
            p_songs = p_songs[0:5]

            categories = playlist_models.ListCategory.objects.all()
            playlists = {}
            for category in categories:
                if category.used:
                    playlists[category.title] = playlist_models.PlayList.objects.filter(
                        category=category
                    ).only("songs")[:4]

            teams = user.teams.all()
            projects = user.projects.all()

            return render(
                request,
                "users/home.html",
                {
                    "user": user,
                    "p_songs": p_songs,
                    "playlists": playlists,
                    "teams": teams,
                    "projects": projects,
                },
            )

    return render(request, "users/home.html", {"user": user})
