from django.contrib import admin
from . import models


@admin.register(models.Team)
class TemaAdmin(admin.ModelAdmin):

    """
    class: TeamAdmin
    author: haein
    des: TeamAdmin Model Definition
    date: 2020-03-27
    """

    list_display = (
        "name",
        "user_list",
        "active_region",
        "is_solo",
    )

    fieldsets = (
        ("Member", {"fields": ("user_list",)}),
        ("Team Info", {"fields": ("name", "active_region", "is_solo")}),
    )

    list_filter = (
        "is_solo",
        "active_region",
    )
