from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from rest_framework import status
from . import serializers
from users import models as user_models


class ListUsersView(APIView, ListModelMixin):
    queryset = user_models.User.objects.all()
    serializer_class = serializers.UserSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request):
        print(request.GET.get("email"))
        if request.GET.get("email") is None:
            page = self.paginate_queryset(self.queryset)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                return self.get_paginated_response(serializer.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            email = {"email": request.GET.get("email")}
            serializer = serializers.EmailSerializer(data=request.GET)

            if serializer.is_valid():
                valid_email = serializer.validated_data.get("email")
                try:
                    user_models.User.objects.get(email=valid_email)
                    return Response(
                        data="중복되는 이메일 입니다.", status=status.HTTP_409_CONFLICT
                    )
                except user_models.User.DoesNotExist:
                    return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def post(self, request):
        serializer = serializers.CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            created_user = serializer.save()
            return Response(created_user, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, "_paginator"):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class MeView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        me = user_models.User.objects.get(pk=request.user)
        serializer = serializers.UserSerializer(me)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserRetrieveView(APIView):
    def get(self, request, pk):
        try:
            users = user_models.User.objects.get(pk=pk)
            serializer = serializers.UserSerializer(users)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except user_models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
