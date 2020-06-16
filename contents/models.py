from django.db import models
from core import models as core_models


TYPE_COVER = "cover"
TYPE_OWN = "own"
TYPE_CLIP = "clip"

TYPE_CHOICES = (
    (TYPE_COVER, "Cover"),
    (TYPE_OWN, "Own"),
    (TYPE_CLIP, "Clip"),
)

PUBLIC = "public"
PRIVATE = "private"
LIMITED = "limited"

EXPOSURE_CHOICES = (
    (PUBLIC, "전체공개"),
    (PRIVATE, "비공개"),
    (LIMITED, "제한공개"),
)


class Content(core_models.TimeStamppedModel):

    """
    class: Content
    author: haein
    des: Base Content Model of the Service
    date: 2020-05-28
    """

    project = models.ForeignKey(
        "projects.Project", related_name="contents", on_delete=models.CASCADE,
    )
    content_file = models.FileField(upload_to="contents")
    content_photo = models.ImageField(upload_to="contents-photo")
    content_title = models.CharField(max_length=64)  # 컨텐츠 제목
    genre = models.ForeignKey(
        "core.Genre", on_delete=models.CASCADE, related_name="contents", default=None,
    )
    description = models.TextField(default="", blank=True)
    lyrics = models.TextField(default="", blank=True)
    exposure_level = models.CharField(
        max_length=16, default=None, choices=EXPOSURE_CHOICES
    )
    content_type = models.CharField(max_length=16, choices=TYPE_CHOICES)

    def __str__(self):
        return self.content_title


class BaseSong(core_models.TimeStamppedModel):

    """
    class: BaseSong
    author: haein
    des: Data set for uploading a song related existed song
    date: 2020-05-28
    """

    title = models.CharField(max_length=64)
    composer = models.CharField(max_length=64, default="", blank=True)
    lyricist = models.CharField(max_length=64, default="", blank=True)
    singer = models.CharField(max_length=64, default="", blank=True)
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Base Song"
        verbose_name_plural = "Base Songs"


# 곡에 대한 추가 정보는 사용자들이 세상에 이미 존재하는 곡들을 커버한 컨텐츠를 올릴때 해당 컨텐츠의 제목과 가수를 찾는 과정에서 입력을 정규화 하기 위해 사용된다.
#
#
#
#
# songs App은 추후에 삭제 해야 된다.
