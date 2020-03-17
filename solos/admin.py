from django.contrib import admin
from . import models as solo_models


@admin.register(solo_models.Solo)
class SoloAdmin(admin.ModelAdmin):
    """
    class: SoloAdmin
    author: haein
    des: Solo Admin
    date: 2020-03-12
    """

    pass
