"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Purchase
from app.serializers import PurchaseSerializer

class PurchaseViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Purchase.filter_permissions(
            super().get_queryset(), Purchase.permission_filters(user))