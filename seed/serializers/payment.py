"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Payment
from app.models import User

class PaymentSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=User.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Payment
        fields = (
            'id',
            'created_at',
            'hash',
            'card_number',
            'expire_date',
            'type',
            'address',
            'bank',
            'name',
            'user_id',  
        )