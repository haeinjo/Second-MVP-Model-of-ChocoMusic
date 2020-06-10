from django.urls import path
from . import views as content_views


app_name = "contents"

urlpatterns = [
    path("create/type/", content_views.AddContentView.as_view(), name="add_content",),
]
