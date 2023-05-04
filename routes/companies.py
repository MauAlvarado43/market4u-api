"""
__Seed builder__
  Extended module
"""

import seed.routes.companies as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.models import Company
from app.serializers import CompanySerializer

class CompanyViewSet(SeedRoute.CompanyViewSet):
    
    # Registry a company
    @action(detail=False, methods=["POST"])
    def registry(self, request):
        data = request.data
        has_fields_or_400(data, "first_name", "last_name", "email", "password")

        first_name = data["first_name"]
        last_name = data["last_name"]
        email = data["email"]
        password = data["password"]

        # code = registry(first_name, last_name, email, password)
        return Response(status=200)
    
    @action(detail=False, methods=["POST"])
    def noservice(self, request):
        return Response(status=200)
        
    

