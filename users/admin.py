from django.contrib import admin
from . import models as user_models


@admin.register(user_models.User)
class UserAdmin(admin.ModelAdmin):
    """
    class: UserAdmin
    author: haein
    des: 사용자 어드민
    date: 2020-03-12
    """

    pass
