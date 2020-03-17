from django.db import models
from core import models as core_models


class BaseSong(core_models.TimeStamppedModel):

    """
    class: BaseSong
    author: haein
    des: BaseSong Model Definition
    date: 2020-03-17
    """

    title = models.CharField(max_length=64)
    composer = models.CharField(max_length=64)
    lyricist = models.CharField(max_length=64)
    singer = models.CharField(max_length=64)
    published_date = models.DateField(auto_now_add=True)


class Song(core_models.TimeStamppedModel):

    """
    class: Song
    author: haein
    des: Song Model Definition
    date: 2020-03-17
    """

    base_song = models.OneToOneField(
        "BaseSong", on_delete=models.CASCADE, related_name="song"
    )  # base_song field will be gotten or created
    album = models.ForeignKey(
        "albums.Album", on_delete=models.CASCADE, related_name="songs"
    )

    def __str__(self):
        return f"{self.album.project.name} - {self.base_song.title}"


class CoveredSong(core_models.TimeStamppedModel):

    """
    class: CoveredSong
    author: haein
    des: CoveredSong Model Definition
    date: 2020-03-17
    """

    base_song = models.ForeignKey(
        "BaseSong", on_delete=models.CASCADE, related_name="covered_songs"
    )
    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="covered_songs"
    )

    def __str__(self):
        return f"{self.project.name} - {self.song.title}"
