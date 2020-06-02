from django.contrib import admin
from . import models


@admin.register(models.FollowingNotification)
class FollowingNotificationAdmin(admin.ModelAdmin):

    """
    class: FollowingNotificationAdmin
    author: haein
    des: Admin Model for FollowingNotification Class
    date: 2020-06-01
    """

    list_display = (
        "receiver",
        "following",
    )

    search_fields = (
        "receiver__alias",
        "receiver__email",
    )


@admin.register(models.OneLikeNotification)
class OneLikeNotificationAdmin(admin.ModelAdmin):

    """
    class: OneLikeNotificationAdmin
    author: haein
    des: Admin Model for OneLikeNotification Class
    date: 2020-06-01
    """

    list_display = (
        "receiver",
        "like_content",
    )

    search_fields = (
        "receiver__alias",
        "receiver__email",
    )


@admin.register(models.MultiLikeNotification)
class MultiLikeNotificationAdmin(admin.ModelAdmin):

    """
    class: MultiLikeNotificationAdmin
    author: haein
    des: Admin Model for MultiLickNotification Class
    date: 2020-06-01
    """

    list_display = ("receiver",)

    search_fields = (
        "receiver_alias",
        "receiver_email",
    )

    filter_horizontal = ("like_contents",)
