"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Variantoption
from app.serializers import VariantoptionSerializer

class VariantoptionViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = VariantoptionSerializer
    queryset = Variantoption.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Variantoption.filter_permissions(
            super().get_queryset(), Variantoption.permission_filters(user))