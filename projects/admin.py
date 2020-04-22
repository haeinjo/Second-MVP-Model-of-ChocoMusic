from django.contrib import admin
from . import models
from songs import models as song_models


class SongInline(admin.TabularInline):
    model = song_models.Song


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):

    """
    class: ProjectAdmin
    author: haein
    des: ProjectAdmin Model Definition
    date: 2020-04-22
    """

    list_display = (
        "title",
        "photo",
    )

    fieldsets = (
        ("Project Info", {"fields": ("title", "description", "photo")}),
        ("By Team", {"fields": ("team",)}),
        ("Participants", {"fields": ("participants",)}),
    )

    filter_horizontal = ("participants",)

    search_fields = (
        "team__name",
        "participants__email",
        "participants__positions__name",
        "participants__genres__name",
        "team__positions__name",
        "team__genres__name",
    )

    inlines = [
        SongInline,
    ]
