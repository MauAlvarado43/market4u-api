"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Shipping
from app.models import Cart
from app.models import User
from app.models import Company

class ShippingSerializer(serializers.ModelSerializer):

    cart_id = serializers.PrimaryKeyRelatedField(
        source='cart', queryset=Cart.objects.all(),
        required=True, allow_null=False)
    buyer_id = serializers.PrimaryKeyRelatedField(
        source='buyer', queryset=User.objects.all(),
        required=False, allow_null=True)
    company_id = serializers.PrimaryKeyRelatedField(
        source='company', queryset=Company.objects.all(),
        required=False, allow_null=True)

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
            'cart_id',
            'buyer_id',
            'company_id',  
        )