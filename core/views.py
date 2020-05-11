from django.shortcuts import render, redirect, reverse
from users import models as user_models
from songs import models as song_models


def intro_view(request):
    return render(request, "intro.html")


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
            p_songs = p_songs[0:4]

            return render(
                request, "users/home.html", {"user": user, "p_songs": p_songs}
            )

    return render(request, "users/home.html", {"user": user})
