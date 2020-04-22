from django.contrib import admin
from . import models


@admin.register(models.RecruitedPosition)
class RecruitedPositionAdmin(admin.ModelAdmin):

    """
    class: RecruitedPositionAdmin
    author: haein
    des: 구인포지션 어드민
    date: 2020-04-22
    """

    list_display = ("number", "position", "recruit")

    fieldsets = (
        ("Base", {"fields": ("number", "position")}),
        ("By", {"fields": ("recruit",)}),
    )


@admin.register(models.Recruit)
class RecruitAdmin(admin.ModelAdmin):

    """
    class: RecruitAdmin
    author: haein
    des: 구인 어드민
    date: 2020-04-22
    """

    list_display = ("title", "active_region", "team")

    fieldsets = (
        (
            "Recruit Info",
            {"fields": ("title", "active_region", "description", "genres")},
        ),
        ("By", {"fields": ("team",)}),
    )

    filter_horizontal = ("genres",)
