from django.db import models
from core import models as core_models


class Team(core_models.TimeStamppedModel):

    """
    class: Team
    author: haein
    des: Team Model to make albums, songs and teams
    date: 2020-03-17
    """

    members = models.ManyToManyField("users.User", related_name="teams")
    leader = models.ForeignKey(
        "users.User", related_name="chef_teams", on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=128)
    active_region = models.CharField(max_length=256)
    genres = models.ManyToManyField("core.Genre")
    avatar = models.ImageField(upload_to="team-profile")
    bio = models.TextField(default="", blank=True)
    is_solo = models.BooleanField(default="True")
    # bestSong = models.ForeignKey(SongInfo...)   SongInfo 구현 필요

    def __str__(self):
        return f"{self.name} at {self.active_region}"
