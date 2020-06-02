from django.db import models
from core import models as core_models


class FollowingNotification(core_models.TimeStamppedModel):

    """
    class: FollowingNotification
    author: haein
    des: Notify Following Information
    date: 2020-06-01
    """

    receiver = models.ForeignKey(
        "users.User", related_name="following_notifications", on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        "users.Following",
        related_name="following_notifications",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.receiver.alias}"


class OneLikeNotification(core_models.TimeStamppedModel):

    """
    class: OneLikeNotification
    author: haein
    des: Notify only one like information
    date: 2020-06-01
    """

    receiver = models.ForeignKey(
        "users.User", related_name="one_like_notifications", on_delete=models.CASCADE
    )
    like_content = models.ForeignKey(
        "comments.LikeContent",
        related_name="one_like_notifications",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.receiver.alias


class MultiLikeNotification(core_models.TimeStamppedModel):

    """
    class: MultiLikeNotification
    author: haein
    des: Notify multi likes information
    date: 2020-06-01
    """

    receiver = models.ForeignKey(
        "users.user", related_name="multi_like_notifications", on_delete=models.CASCADE
    )
    like_contents = models.ManyToManyField(
        "comments.LikeContent", related_name="multi_like_notifications"
    )

    def __str__(self):
        return self.receiver.alias
