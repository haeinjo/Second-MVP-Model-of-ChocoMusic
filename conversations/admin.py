from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """
    class: ConversationAdmin
    author: haein
    des: 대화 어드민
    date: 2020-04-22
    """

    filter_horizontal = ("users",)


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """
    class: MessageAdmin
    author: haein
    des: 메세지 어드민
    date: 2020-04-22
    """

    pass
