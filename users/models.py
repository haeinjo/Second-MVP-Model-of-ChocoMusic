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

    email = models.EmailField(max_length=256, unique=True)  # unique 부분에 대해서는 추후 상의가 필요함
    name = models.CharField(max_length=64)
    alias = models.CharField(max_length=64)
    age = models.IntegerField()
    address = models.CharField(max_length=128)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)  # choice 항목 상의
    avatar = models.ImageField()
    # images --- 추후 개발 및 상의 필요

    def __str__(self):
        return "%s - %s" % (self.email, self.name)
