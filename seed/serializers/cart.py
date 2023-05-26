"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Cart
from app.models import User

class CartSerializer(serializers.ModelSerializer):

    shipping_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='shippings', read_only=True)

    buyer_id = serializers.PrimaryKeyRelatedField(
        source='buyer', queryset=User.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Cart
        fields = (
            'id',
            'created_at',
            'hash',
            'payment',
            'buyer_id',
            'shipping_ids',  
        )