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
    composer = models.CharField(max_length=64, null=True, blank=True)
    lyricist = models.CharField(max_length=64, null=True, blank=True)
    singer = models.CharField(max_length=64, null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Base Song"
        verbose_name_plural = "Base Songs"


# 프로젝트를 앨범으로 봤을때
# 앨범에 참여한 인원의 역할이 모든 곡에서 동일함을 보장할 수 없다.
# 뮤지션의 포지션과는 무관하게 현제 곡에서 뮤지션(유저)의 역할을 나타낸다.
# 포지션이 보컬인 뮤지션이 현재 곡에서 작자 또는 작곡을 했을 수 도 있다.
class Role(core_models.TimeStamppedModel):

    """
    class: Role
    author: haein
    des: Match users with a role
    date: 2020-03-19
    """

    users = models.ManyToManyField("users.User", related_name="roles")
    position = models.ForeignKey(
        "core.Position", on_delete=models.CASCADE, related_name="roles", default=None,
    )
    song = models.ForeignKey(
        "songs.Song", on_delete=models.CASCADE, related_name="roles", default=None
    )

    def __str__(self):
        users = self.users.all()
        usernames = []
        for user in users:
            usernames.append(user.alias)
        return f"{self.position.name}: {', '.join(usernames)}"


class Song(core_models.TimeStamppedModel):

    """
    class: Song
    author: haein
    des: Song Model Definition
    date: 2020-04-22
    """

    base_song = models.ForeignKey(
        "BaseSong", on_delete=models.CASCADE, related_name="covered_songs", default=None
    )  # BaseSong에 등록되어있지 않은 커버곡을 업로드할 경우 업로드되는 곡에 대한 정보가 BaseSong에 저장되어야 된다.
    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="covered_songs"
    )
    is_covered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.project.title} - {self.base_song.title}"
