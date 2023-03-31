"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Payment
from app.serializers import PaymentSerializer

class PaymentViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Payment.filter_permissions(
            super().get_queryset(), Payment.permission_filters(user))