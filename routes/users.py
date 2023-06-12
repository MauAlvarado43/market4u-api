"""
__Seed builder__
  Extended module
"""

from django.contrib.auth import authenticate
import seed.routes.users as SeedRoute
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.models import User
from app.serializers import UserSerializer
from domain.create_user import registry, registry_generate, registry_verify
from domain.recover_password import send_token_password, restore_password
from domain.utils import http_codes
from domain.update_user import update_info

from domain.update_user_superadmin import update_info_superadmin
from domain.update_user_normal import update_info_normal
from domain.create_user_superadmin import create_info_superadmin
from domain.create_user_company import create_info_company
from domain.add_products_wishlist import add_products_wishlist
from domain.update_shipping import update_info_shipping

class UserViewSet(SeedRoute.UserViewSet):
    

    @action(detail=False, methods=["POST"])
    def login(self, request):
        data = request.data
        has_fields_or_400(data, "email", "password")

        email = data["email"]
        password = data["password"]

        user = authenticate(username=email, password=password)
        print(user)
        company = user.company

        try:
            token = Token.objects.get(user=user)
        except Exception as error:
            print(error)
            token = Token.objects.create(user=user)

        if user.token_verified:
            return Response(
                status=status.HTTP_200_OK, 
                data={
                    "key": token.key, 
                    "user": user.id, 
                    "company": None if company is None else company.id,
                    "type": user.type
                }
            )

        return Response(status=http_codes.CODE_220_TOKEN_NOT_VERIFIED, data={ "token": user.token })

    @action(detail=False, methods=["POST"])
    def signup(self, request):
        data = request.data
        has_fields_or_400(data, "first_name", "last_name", "email", "password")

        first_name = data["first_name"]
        last_name = data["last_name"]
        email = data["email"]
        password = data["password"]

        response = registry(first_name, last_name, email, password)
        return Response(status=response["status"], data={"token": response["token"]})

    @action(detail=False, methods=["POST"])
    def registry_verify(self, request):
        data = request.data
        has_fields_or_400(data, "token", "code")

        token = data["token"]
        code = data["code"]

        http_code = registry_verify(token, code)
        return Response(status=http_code)

    @action(detail=False, methods=["POST"])
    def registry_generate(self, request):
        data = request.data
        has_fields_or_400(data, "token")

        token = data["token"]
        code = registry_generate(token)
        return Response(status=code)

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
    
    @action(detail=False, methods=['POST'])
    def update_user(self, request):
      data=request.data
      has_fields_or_400(data, 'user_id', 'city', 'cologn', 'cp', 'firstName', 'lastName', 'municipality', 
                        'state', 'street', 'telephone', 'password')
      update_info(data['user_id'], data['city'], data['cologn'], data['cp'], data['firstName'], data['password'],
                  data['lastName'], data['municipality'], data['state'], data['street'], data['telephone'])
      return Response(status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'])
    def update_user_superadmin(self,request):
        data = request.data
        has_fields_or_400(data, 'user_id', 'company_id', 'email', 'firstName', 'lastName', 'type', 'username', 'password')
        update_info_superadmin(data['user_id'], data['company_id'], data['email'], data['firstName'], data['lastName'], data['type'], data['username'], data['password'])
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'])
    def update_user_normal(self,request):
        data = request.data
        has_fields_or_400(data, 'user_id', 'email', 'firstName', 'lastName', 'type', 'password', 'company_id')
        update_info_normal(data['user_id'], data['email'], data['firstName'], data['password'],data['lastName'], data['type'], data['company_id'])
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'])
    def create_user_superadmin(self,request):
        data = request.data
        has_fields_or_400(data, 'company_id', 'email', 'firstName', 'lastName', 'password', 'type')
        create_info_superadmin(data['company_id'], data['email'], data['firstName'], data['lastName'], data['password'], data['type'])
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'])
    def create_user_company(self,request):
        data = request.data
        has_fields_or_400(data, 'company_id', 'email', 'firstName', 'lastName', 'password', 'type')
        create_info_company( data['company_id'], data['email'], data['firstName'], data['lastName'], data['password'], data['type'])
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def add_products_wishlist(self,request):
        data=request.data
        has_fields_or_400(data, 'user_id', 'product_id')
        exist_product = add_products_wishlist(data['user_id'], data['product_id'])
        return Response(status=status.HTTP_200_OK, data={'exist_product': exist_product})
    
    @action(detail=False, methods=['POST'])
    def add_info_shipping(self,request):
        data = request.data
        has_fields_or_400(data,'shipping_id','info')
        update_info_shipping(data['shipping_id'],data['info'])
        return Response(status=status.HTTP_200_OK)