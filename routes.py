"""
__Seed builder__
  Extended module
"""

import seed.routes. as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.models import 
from app.serializers import Serializer

class ViewSet(SeedRoute.ViewSet):
    pass