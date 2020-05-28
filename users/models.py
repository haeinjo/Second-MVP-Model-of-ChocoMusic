from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    class: User(custom)
    author: haein
    des: 사용자
    date: 2020-03-12
    """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    email = models.EmailField(max_length=256)  # unique 부분에 대해서는 추후 상의가 필요함
    alias = models.CharField(max_length=64)
    address = models.CharField(max_length=128, blank=True, default="")
    bio = models.TextField(default="", blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)  # choice 항목 상의
    avatar = models.ImageField(upload_to="user-profile")
    birthdate = models.DateField(blank=True, null=True)
    positions = models.ManyToManyField(
        "core.Position", related_name="users", blank=True
    )
    genres = models.ManyToManyField("core.Genre", related_name="users", blank=True)
    is_varified = models.BooleanField(default=False)
    is_first = models.BooleanField(default=True)
    email_login = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}"

    def random_records(self):
        return self.objects.random_records(self)


class ActiveRegion(models.Model):
    """
    class: ActiveRegion
    author: haein
    des: 유저의 활동지역
    date: 2020-05-27
    """

    user = models.ForeignKey(
        "users.User", related_name="active_regions", on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        "core.City", related_name="active_reigions", on_delete=models.CASCADE
    )
    borough = models.ForeignKey(
        "core.Borough", related_name="active_regions", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} - {self.city} {self.borough}"
