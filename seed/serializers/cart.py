"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Cart
from app.models import User
from app.models import Payment

class CartSerializer(serializers.ModelSerializer):

    shipping_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='shippings', read_only=True)

    buyer_id = serializers.PrimaryKeyRelatedField(
        source='buyer', queryset=User.objects.all(),
        required=True, allow_null=False)
    payment_id = serializers.PrimaryKeyRelatedField(
        source='payment', queryset=Payment.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Cart
        fields = (
            'id',
            'created_at',
            'hash',
            'buyer_id',
            'payment_id',
            'shipping_ids',  
        )