"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Sale
from app.models import Product
from app.models import User

class SaleSerializer(serializers.ModelSerializer):

    product_id = serializers.PrimaryKeyRelatedField(
        source='product', queryset=Product.objects.all(),
        required=True, allow_null=False)
    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=User.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Sale
        fields = (
            'id',
            'created_at',
            'hash',
            'disscount',
            'start_date',
            'end_date',
            'product_id',
            'user_id',  
        )