"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Product
from app.serializers import ProductSerializer

class ProductViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Product.filter_permissions(
            super().get_queryset(), Product.permission_filters(user))