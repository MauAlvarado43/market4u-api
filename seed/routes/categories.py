"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Category
from app.serializers import CategorySerializer

class CategoryViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Category.filter_permissions(
            super().get_queryset(), Category.permission_filters(user))