from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models as user_models


@admin.register(user_models.User)
class CustomUserAdmin(UserAdmin):
    """
    class: UserAdmin
    author: haein
    des: 사용자 어드민
    date: 2020-03-12
    """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "alias",
                    "birthdate",
                    "address",
                    "gender",
                    "avatar",
                    "positions",
                    "genres",
                    "bio",
                )
            },
        ),
    )

    list_display = UserAdmin.list_display + (
        "alias",
        "birthdate",
        "address",
        "gender",
        "avatar",
    )
