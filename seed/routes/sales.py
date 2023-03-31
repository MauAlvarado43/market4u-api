"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Sale
from app.serializers import SaleSerializer

class SaleViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Sale.filter_permissions(
            super().get_queryset(), Sale.permission_filters(user))