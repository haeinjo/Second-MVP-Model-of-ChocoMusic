from django.contrib import admin
from . import models


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):

    """
    class: TeamAdmin
    author: haein
    des: TeamAdmin Model Definition
    date: 2020-03-27
    """

    list_display = (
        "name",
        "avatar",
        "active_region",
        "is_solo",
    )

    fieldsets = (
        ("Member", {"fields": ("users",)}),
        (
            "Team Info",
            {"fields": ("name", "active_region", "is_solo", "positions", "genres")},
        ),
    )

    list_filter = ("is_solo",)

    search_fields = ("name", "users__email", "genres__name", "positions__name")

    filter_horizontal = ("users", "positions", "genres")
