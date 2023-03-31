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

    purchase_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='purchases', read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=User.objects.all(),
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
            'destiny',
            'purchase_ids',
            'user_id',
            'payment_id',  
        )