from django.contrib import admin
from . import models


@admin.register(models.ListCategory)
class ListCategoryAdmin(admin.ModelAdmin):

    """
    class: ListCategoryAdmin
    author: haein
    des: ListCategoryAdmin Model Definition
    date: 2020-04-30
    """

    pass


@admin.register(models.PlayList)
class PlayListAdmin(admin.ModelAdmin):

    """
    class: PlayListAdmin
    author: haein
    des: PlayListAdmin Model Definition
    date: 2020-04-30
    """

    list_display = ("title", "category", "description")

    search_fields = (
        "songs__title",
        "user__alias",
        "title",
        "category",
    )

    filter_horizontal = ("songs",)

    fieldsets = (
        ("List Info", {"fields": ("title", "category", "description")}),
        ("Made by", {"fields": ("user",)}),
        ("Songs", {"fields": ("songs",)}),
    )
