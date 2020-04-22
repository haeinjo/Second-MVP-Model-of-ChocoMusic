from django.contrib import admin
from . import models


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper


@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):

    """
    class: PositionAdmin
    author: haein
    des: 포지션 어드민
    date: 2020-04-22
    """

    pass


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):

    """
    class: GenreAdmin
    author: haein
    des: 장르 어드민
    date: 2020-04-22
    """

    pass
