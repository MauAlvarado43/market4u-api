"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Shipping
from app.models import User
from app.models import Cart

class ShippingSerializer(serializers.ModelSerializer):

    seller_id = serializers.PrimaryKeyRelatedField(
        source='seller', queryset=User.objects.all(),
        required=True, allow_null=False)
    cart_id = serializers.PrimaryKeyRelatedField(
        source='cart', queryset=Cart.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Shipping
        fields = (
            'id',
            'created_at',
            'hash',
            'info',
            'folio',
            'address',
            'status',
            'seller_id',
            'cart_id',  
        )