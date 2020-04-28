from django.contrib import admin
from . import models
from core import admin as core_admin


@admin.register(models.BaseSong)
class BaseSongAdmin(admin.ModelAdmin):

    """
    class: BaseSongAdmin
    author: haein
    des: 노래객체의 베이스가 되는 어드민
    date: 2020-04-22
    """

    list_display = ("title", "singer", "published_date")

    search_fields = ("title", "singer", "composer", "lyricist")


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):

    """
    class: RoleAdmin
    author: haein
    des: 노래에서의 역할 어드민
    date: 2020-04-22
    """

    filter_horizontal = ("users",)
    list_filter = (("position__name", core_admin.custom_titled_filter("Position")),)
    search_fields = ("users__email", "users__alia", "position__name")


class RoleInline(admin.TabularInline):
    model = models.Role


@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):

    """
    class: SongAdmin
    author: haein
    des: 노래 어드민
    date: 2020-04-22
    """

    list_display = ("project", "base_song", "is_covered")

    inlines = [
        RoleInline,
    ]

    fieldsets = (
        ("By", {"fields": ("project",)}),
        ("Song Info", {"fields": ("base_song",)}),
    )
    search_fields = (
        "base_song__title",
        "base_song__composer",
        "base_song__lyricist",
        "base_song__singer",
        "roles__name",
    )

    list_filter = ("is_covered",)
