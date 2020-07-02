from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models


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

    LOGIN_GOOGLE = "google"
    LOGIN_KAKAO = "kakao"
    LOGIN_EMAIL = "email"

    LOGIN_CHOICES = (
        (LOGIN_GOOGLE, "Google"),
        (LOGIN_KAKAO, "Kakao"),
        (LOGIN_EMAIL, "Email"),
    )

    email = models.EmailField(max_length=256)  # unique 부분에 대해서는 추후 상의가 필요함
    alias = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, default="")
    bio = models.TextField(default="", blank=True)
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, blank=True, default=""
    )  # choice 항목 상의
    avatar = models.ImageField(upload_to="user-profile", blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    positions = models.ManyToManyField(
        "core.Position", related_name="users", blank=True
    )
    genres = models.ManyToManyField("core.Genre", related_name="users", blank=True)
    borough = models.ManyToManyField("core.Borough", related_name="users", blank=True)
    email_varified = models.BooleanField(default=False)
    phone_varified = models.BooleanField(default=False)
    is_first = models.BooleanField(default=True)
    login_method = models.CharField(max_length=16, choices=LOGIN_CHOICES, default="")

    def __str__(self):
        return f"{self.email}"

    def random_records(self):
        return self.objects.random_records(self)


class Following(core_models.TimeStamppedModel):

    """
    class: FollowUser
    author: haein
    des: Follow to User
    date: 2020-05-28
    """

    targetUser = models.ForeignKey(
        "User", related_name="followers", on_delete=models.CASCADE
    )
    follower = models.ForeignKey(
        "User", related_name="followings", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.targetUser.alias
