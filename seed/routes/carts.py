"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Cart
from app.serializers import CartSerializer

class CartViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Cart.filter_permissions(
            super().get_queryset(), Cart.permission_filters(user))