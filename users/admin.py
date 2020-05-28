from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models as user_models
from core import admin as core_admin


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
        "is_varified",
        "is_first",
    )

    filter_horizontal = (
        "positions",
        "genres",
    )

    search_fields = UserAdmin.search_fields + ("positions__name", "genres__name",)

    list_filter = UserAdmin.list_filter + (
        ("positions__name", core_admin.custom_titled_filter("Position")),
        ("genres__name", core_admin.custom_titled_filter("Genre")),
    )

    ordering = ("-date_joined",)
