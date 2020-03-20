from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStamppedModel):

    """
    class: Conversation
    author: haein
    des: Conversation Model Definition
    date: 2020-03-20
    """

    title = models.CharField(max_length=64)
    users = models.ManyToManyField("users.User", related_name="conversations")

    def __str__(self):
        users = self.users.all()
        user_list = []

        for user in users:
            user_list.append(user.alias)

        return f"{', '.join(user_list)}"


class Message(core_models.TimeStamppedModel):

    """
    class: Message
    author: haein
    des: Message Model
    date: 2020-03-20
    """

    message = models.TextField()
    conversation = models.ForeignKey(
        "Conversation", on_delete=models.CASCADE, related_name="messages"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="messages"
    )

    def __str__(self):
        return f"{self.user.alias} - {self.conversation.title}"
