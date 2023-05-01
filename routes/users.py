import seed.routes.users as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.models import User
from app.serializers import UserSerializer
from domain.update_user import update_info

class UserViewSet(SeedRoute.UserViewSet):
    @action(detail=False, methods=['POST'])
    def update_user(self, request):
      data=request.data
      print(data)
      has_fields_or_400(data, 'user_id', 'city', 'cologn', 'cp', 'email', 'firstName', 'lastName', 'municipality', 
                        'state', 'street', 'telephone', 'type', 'password', 'company')
      update_info(data['user_id'], data['city'], data['cologn'], data['cp'], data['email'], data['firstName'], data['password'],
                  data['lastName'], data['municipality'], data['state'], data['street'], data['telephone'], data['type'], data['company'])
      return Response(status=status.HTTP_200_OK)