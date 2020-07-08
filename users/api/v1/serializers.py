from rest_framework import serializers
from users import models as user_models
from core import models as core_models


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.Genre
        fields = ("name",)


class UserSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = user_models.User
        fields = (
            "genres",
            "email",
        )


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = "__all__"

    def create(self, validated_data):
        try:
            created_user = user_models.User.objects.create_user(**validated_data)
            print(validated_data)
            created_user.set_password(validated_data.get("password"))
            created_user.save()
            return created_user
        except Exception:
            return None


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = ("email",)
