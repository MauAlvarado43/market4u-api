"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Opinion
from app.serializers import OpinionSerializer

class OpinionViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = OpinionSerializer
    queryset = Opinion.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Opinion.filter_permissions(
            super().get_queryset(), Opinion.permission_filters(user))