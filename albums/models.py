from django.db import models
from core import models as core_models


class Album(core_models.TimeStamppedModel):

    """
    class: Album
    author: haein
    des: Album Model Definition
    date: 2020-03-17
    """

    title = models.CharField(max_length=64)
    description = models.TextField()
    photo = models.ImageField()
    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="albums"
    )

    def __str__(self):
        return f"{self.project.name} - {self.title}"
