from django.urls import path
from . import views as content_views


app_name = "contents"

urlpatterns = [
    path(
        "create/type/",
        content_views.AddContentTypeView.as_view(),
        name="add_type_content",
    ),
    path(
        "create/file/",
        content_views.AddContentFileView.as_view(),
        name="add_file_content",
    ),
    path(
        "create/info/",
        content_views.AddContentInfoView.as_view(),
        name="add_info_content",
    ),
    path(
        "create/check/",
        content_views.AddContentCheckView.as_view(),
        name="add_check_content",
    ),
    path("create/", content_views.AddContentView.as_view(), name="add_content",),
]
