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

    KAKAO_LOGIN = "kakao"
    GOOGLE_LOGIN = "google"
    EMAIL_LOGIN = "email"

    LOGIN_CHOICES = (
        (KAKAO_LOGIN, "Kakao"),
        (GOOGLE_LOGIN, "Google"),
        (EMAIL_LOGIN, "Email"),
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
    borough = models.ManyToManyField("core.Borough", related_name="users")
    email_varified = models.BooleanField(default=False)
    phone_varified = models.BooleanField(default=False)
    is_first = models.BooleanField(default=True)
    login_method = models.CharField(
        max_length=8, choices=LOGIN_CHOICES, default=EMAIL_LOGIN
    )

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
