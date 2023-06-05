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
from domain.fiel_check import validate_keys
from domain.create_company import create_company

class CompanyViewSet(SeedRoute.CompanyViewSet):
    
    @action(detail=False, methods=["POST"])
    def registry(self, request):
        data = request.data
        has_fields_or_400(data, "company", "user", "validation")

        company = data["company"]
        user = data["user"]
        validation = data["validation"]

        print(data)
        code = create_company(company, user, validation)
        return Response(status=code)
    
    @action(detail=False, methods=["POST"])
    def noservice(self, request):
        return Response(status=200)
        
    @action(detail=False, methods=["POST"])
    def validate_field(self, request):
        data = request.data
        has_fields_or_400(data, "certificate", "private_key", "password")
        result = validate_keys(data["certificate"], data["private_key"], data["password"])