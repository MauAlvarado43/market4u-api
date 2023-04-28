"""
__Seed builder__
  Extended module
"""

from django.contrib.auth import authenticate
import seed.routes.users as SeedRoute
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.models import User
from app.serializers import UserSerializer


class UserViewSet(SeedRoute.UserViewSet):

    @action(detail=False, methods=["POST"])
    def login(self, request):
        data = request.data
        has_fields_or_400(data, "email", "password")

        email = data["email"]
        password = data["password"]

        user = authenticate(username=email, password=password)

        try:
            token = Token.objects.get(user=user)
        except Exception as error:
            print(error)
            token = Token.objects.create(user=user)

    @action(detail=False, methods=["POST"])
    def registry(self, request):
        data = request.data
        has_fields_or_400(data, "first_name", "last_name", "email", "password")

        first_name = data["first_name"]
        last_name = data["last_name"]
        email = data["email"]
        password = data["password"]

        code = registry(first_name, last_name, email, password)
        return Response(status=code)

    @action(detail=False, methods=["POST"])
    def registry_verify(self, request):
        data = request.data
        has_fields_or_400(data, "token", "code")

        token = data["token"]
        code = data["code"]

        http_code = registry_verify(token)
        return Response(status=http_code)
    
    @action(detail=False, methods=["POST"])
    def recover_password(self, request):
        data = request.data
        has_fields_or_400(data, "email")

        email = data["email"]
        code = send_token_password(email)
        return Response(status=code)

    @action(detail=False, methods=["POST"])
    def restore_password(self, request):
        data = request.data
        has_fields_or_400(data, "token", "new_password")

        token = data["token"]
        new_password = data["new_password"]
        code = restore_password(token, new_password)
        return Response(status=code)





