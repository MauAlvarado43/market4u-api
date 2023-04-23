"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Shipping
from app.serializers import ShippingSerializer

class ShippingViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = ShippingSerializer
    queryset = Shipping.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Shipping.filter_permissions(
            super().get_queryset(), Shipping.permission_filters(user))