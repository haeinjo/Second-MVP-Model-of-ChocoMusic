from django.db import models
from core import models as core_models


class Genre(core_models.AbstractItem):
    """
    class: Genre
    author: haein
    des: 장르
    date: 2020-03-12
    """

    pass


class Position(core_models.AbstractItem):
    """
    class: Position
    author: haein
    des: 음악 역량
    date: 2020-03-12
    """

    pass


class Solo(core_models.TimeStamppedModel):
    """
    class: Solo
    author: haein
    des: 가수
    date: 2020-03-12
    """

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="solos",
    )
    name = models.CharField(max_length=128)
    activeRegion = models.CharField(max_length=256)
    positions = models.ManyToManyField("Position")
    genres = models.ManyToManyField("Genre")
    avatar = models.ImageField()
    # bestSong = models.ForeignKey(SongInfo...)   SongInfo 구현 필요

    def __str__(self):
        return f"{self.Name} at {self.activeRegion}"
