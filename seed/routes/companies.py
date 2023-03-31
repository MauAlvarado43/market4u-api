"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Company
from app.serializers import CompanySerializer

class CompanyViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Company.filter_permissions(
            super().get_queryset(), Company.permission_filters(user))