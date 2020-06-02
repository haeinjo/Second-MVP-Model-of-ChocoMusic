from django.contrib import admin
from . import models


@admin.register(models.CommentToContent)
class CommentToContentAdmin(admin.ModelAdmin):

    """
    class: CommentToContentAdmin
    author: haein
    des: Admin Model for CommentTocontent Class
    date: 2020-06-01
    """

    list_display = (
        "writer",
        "content",
    )

    search_fields = (
        "writer__alias",
        "writer__email",
        "content__content_title",
    )


@admin.register(models.LikeContent)
class LikeContentAdmin(admin.ModelAdmin):

    """
    class: LikeContentAdmin
    author: haein
    des: Admin Model for LikeContent Class
    date: 2020-06-01
    """

    list_display = (
        "sender",
        "target_content",
    )

    search_fields = ("sender__alias", "sender__email", "target_content__content_title")


@admin.register(models.HateContent)
class HateContentAdmin(admin.ModelAdmin):

    """
    class: HateContentAdmin
    author: haein
    des: Admin Model for HateContent Class
    date: 2020-06-01
    """

    list_display = (
        "sender",
        "target_content",
    )

    search_fields = ("sender__alias", "sender__email", "target_content__content_title")
