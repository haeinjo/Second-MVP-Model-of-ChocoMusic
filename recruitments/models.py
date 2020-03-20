from django.db import models
from core import models as core_models


class RecruitedPosition(core_models.TimeStamppedModel):

    """
    class: RecruitedPosition
    author: haein
    des: Model to Match Position with Volume for Recruitment
    date: 2020-03-20
    """

    number = models.IntegerField()
    position = models.ForeignKey(
        "core.Position", on_delete=models.CASCADE, related_name="recruited_positions"
    )


class Recruit(core_models.TimeStamppedModel):

    """
    class: Recruit
    author: haein
    des: Recruit Model Definition
    date: 2020-03-20
    """

    title = models.CharField(max_length=64)
    active_region = models.CharField(max_length=128)
    description = models.TextField()
    genres = models.ManyToManyField("core.Genre", related_name="recruits")
    positions = models.ManyToManyField("RecruitedPosition", related_name="recruits")
    team = models.ForeignKey(
        "teams.Team", on_delete=models.CASCADE, related_name="recruits"
    )
