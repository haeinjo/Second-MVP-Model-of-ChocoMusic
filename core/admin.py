from django.contrib import admin
from . import models
from core import models as core_models


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


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):

    """
    class: TagAdmin
    author: haein
    des: 태그 어드민
    date: 2020-06-06
    """

    pass


class BoroughInline(admin.TabularInline):
    model = core_models.Borough


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):

    """
    class: CityAdmin
    author: haein
    des: 시 어드민
    date: 2020-06-06
    """

    inlines = [
        BoroughInline,
    ]


@admin.register(models.Borough)
class BoroughAdmin(admin.ModelAdmin):

    """
    class: BoroughAdmin
    author: haein
    des: 구 어드민
    date: 2020-06-06
    """

    pass


@admin.register(models.LoginMethod)
class LoginMethodAdmin(admin.ModelAdmin):

    """
    class: LoginMethodAdmin
    author: haein
    des: LoginMethod admin
    date: 2020-06-25
    """

    pass
