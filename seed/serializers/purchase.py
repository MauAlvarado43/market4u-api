"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Purchase
from app.models import Shipping

class PurchaseSerializer(serializers.ModelSerializer):

    shipping_id = serializers.PrimaryKeyRelatedField(
        source='shipping', queryset=Shipping.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Purchase
        fields = (
            'id',
            'created_at',
            'hash',
            'amount',
            'product',
            'sale',
            'shipping_id',  
        )