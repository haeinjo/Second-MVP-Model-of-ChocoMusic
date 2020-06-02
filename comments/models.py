from django.db import models
from core import models as core_models


class CommentToContent(core_models.TimeStamppedModel):

    """
    class: Comment
    author: haein
    des: Comment Model to a content
    date: 2020-05-29
    """

    writer = models.ForeignKey(
        "users.User", related_name="comments", on_delete=models.CASCADE
    )
    comment = models.TextField()
    content = models.ForeignKey(
        "contents.Content", related_name="comments", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.writer.alias} - {self.content.content_title}"


class LikeContent(core_models.TimeStamppedModel):

    """
    class: LikeContent
    author: haein
    des: LikeContent Model to like a content
    date: 2020-06-01
    """

    sender = models.ForeignKey(
        "users.User", related_name="like_contents", on_delete=models.CASCADE
    )
    target_content = models.ForeignKey(
        "contents.Content", related_name="like_contents", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.sender.alias} - {self.target_content.content_title}"


class HateContent(core_models.TimeStamppedModel):

    """
    class: HateContent
    author: haein
    des: HateContent Model to hate a content
    date: 2020-06-01
    """

    sender = models.ForeignKey(
        "users.User", related_name="hate_contents", on_delete=models.CASCADE
    )
    target_content = models.ForeignKey(
        "contents.Content", related_name="hate_contents", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.sender.alias} - {self.target_content.content_title}"
