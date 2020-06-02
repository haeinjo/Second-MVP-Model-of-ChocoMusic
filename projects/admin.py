from django.contrib import admin
from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):

    """
    class: ProjectAdmin
    author: haein
    des: ProjectAdmin Model Definition
    date: 2020-04-22
    """

    list_display = ("title",)

    fieldsets = (
        ("Project Info", {"fields": ("title", "description")}),
        ("By Team", {"fields": ("team",)}),
    )

    search_fields = (
        "team__name",
        "team__positions__name",
        "team__genres__name",
    )
