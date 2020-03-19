from django.db import models
from core import models as core_models


class Team(core_models.TimeStamppedModel):

    """
    class: Team
    author: haein
    des: Team Model to make albums, songs and teams
    date: 2020-03-17
    """

    user = models.ManyToManyField("users.User", related_name="projects")
    name = models.CharField(max_length=128)
    activeRegion = models.CharField(max_length=256)
    positions = models.ManyToManyField("core.Position")
    genres = models.ManyToManyField("core.Genre")
    avatar = models.ImageField()
    is_solo = models.BooleanField()
    # bestSong = models.ForeignKey(SongInfo...)   SongInfo 구현 필요

    def __str__(self):
        return f"{self.Name} at {self.activeRegion}"
