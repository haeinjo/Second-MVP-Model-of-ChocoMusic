from django.db import models
from core import models as core_models
from projects import models as project_models


class ListCategory(core_models.TimeStamppedModel):

    """
    class: ListCategory
    author: haein
    des: ListCategory Model Definition
    date: 2020-04-30
    """

    title = models.CharField(max_length=32)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class PlayList(core_models.TimeStamppedModel):

    """
    class: PlayList
    author: haein
    des: PlayList Model Definition
    date: 2020-04-30
    """

    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(
        "ListCategory", on_delete=models.CASCADE, related_name="paly_lists"
    )
    songs = models.ManyToManyField("songs.Song", related_name="play_lists")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="play_lists"
    )

    def __str__(self):
        return f"{self.title} - {self.description}"

    def first_song_photo(self):
        song = self.songs.all()[:1]
        project = project_models.Project.objects.get(songs=song)
        return project.photo
