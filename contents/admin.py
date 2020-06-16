from django.contrib import admin
from . import models


@admin.register(models.BaseSong)
class BaseSongAdmin(admin.ModelAdmin):

    """
    class: BaseSongAdmin
    author: haein
    des: 노래객체의 베이스가 되는 어드민
    date: 2020-05-28
    """

    list_display = ("title", "singer", "published_date")

    search_fields = ("title", "singer", "composer", "lyricist")


@admin.register(models.Content)
class ContentAdmin(admin.ModelAdmin):

    """
    class: ContentAdmin
    author: haein
    des: Admin for Content Model
    date: 2020-05-28
    """

    list_display = (
        "content_title",
        "project",
        "content_type",
        "exposure_level",
    )

    fieldsets = (
        ("By", {"fields": ("project",)}),
        ("Song Info", {"fields": ("description", "lyrics", "genres")}),
    )
    search_fields = (
        "project__title",
        "content_title",
        "content_type",
    )

    list_filter = ("content_type", "exposure_level")
