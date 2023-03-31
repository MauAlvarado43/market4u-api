"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Opinion
from app.models import Product
from app.models import User

class OpinionSerializer(serializers.ModelSerializer):

    product_id = serializers.PrimaryKeyRelatedField(
        source='product', queryset=Product.objects.all(),
        required=True, allow_null=False)
    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=User.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Opinion
        fields = (
            'id',
            'created_at',
            'hash',
            'title',
            'description',
            'rate',
            'product_id',
            'user_id',  
        )