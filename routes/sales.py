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
from domain.utils import http_codes


class SaleViewSet(SeedRoute.SaleViewSet):
    
    @action(detail=False, methods=["POST"])
    def nullable_products(self,request):
        data = request.data 
        print(data)
        has_fields_or_400(data,'sale_id')
        return Response(status=status.HTTP_200_OK)