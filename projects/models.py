from django.db import models
from core import models as core_models


class Project(core_models.TimeStamppedModel):

    """
    class: Project
    author: haein
    des: Project Model to make project
    date: 2020-03-19
    """

    title = models.CharField(max_length=128)
    description = models.TextField()
    photo = models.ImageField()
    team = models.ForeignKey(
        "teams.Team", on_delete=models.CASCADE, related_name="projects"
    )
    participants = models.ManyToManyField("users.User", related_name="projects")

    def __str__(self):
        return f"{self.team.name} - {self.title}"
