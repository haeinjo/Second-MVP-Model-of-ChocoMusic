from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models


active_region = {
    "서울특별시": [
        "종로구",
        "중구",
        "용산구",
        "성동구",
        "광진구",
        "동대문구",
        "중랑구",
        "성북구",
        "강북구",
        "도봉구",
        "노원구",
        "은평구",
        "서대문구",
        "마포구",
        "양천구",
        "강서구",
        "구로구",
        "금천구",
        "영등포구",
        "동작구",
        "관악구",
        "서초구",
        "강남구",
        "송파구",
        "강동구",
    ],
    "부산광역시": [
        "중구",
        "서구",
        "동구",
        "영도구",
        "부산진구",
        "동래구",
        "남구",
        "북구",
        "강서구",
        "해운대구",
        "사하구",
        "금정구",
        "연제구",
        "수영구",
        "사상구",
        "기장군",
    ],
    "대구광역시": ["중구", "동구", "서구", "남구", "북고", "수성구", "달서구", "달성군"],
    "인천광역시": ["중구", "동구", "미주홀구", "연수구", "남동구", "부평구", "계양구", "서구", "강화군", "옹진군"],
    "광주광역시": ["동구", "서구", "남구", "북고", "광산구"],
    "대전광역시": ["동구", "중구", "서구", "유성구", "대덕구"],
    "울산광역시": ["중구", "남구", "동구", "북구", "울주군"],
    "세종특별자치시": ["세종시"],
}


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
    city = models.CharField(max_length=16, blank=True, default="")
    borough = models.CharField(max_length=16, blank=True, default="")
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
