"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Variant
from app.serializers import VariantSerializer

class VariantViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = VariantSerializer
    queryset = Variant.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Variant.filter_permissions(
            super().get_queryset(), Variant.permission_filters(user))