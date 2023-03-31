"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Purchase
from app.models import Cart

class PurchaseSerializer(serializers.ModelSerializer):

    cart_id = serializers.PrimaryKeyRelatedField(
        source='cart', queryset=Cart.objects.all(),
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
            'cart_id',  
        )