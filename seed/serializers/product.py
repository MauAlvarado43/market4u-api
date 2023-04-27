"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Product
from app.models import User
from app.models import Sale
from app.models import Category

class ProductSerializer(serializers.ModelSerializer):

    opinion_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='opinions', read_only=True)
    variant_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='variants', read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=User.objects.all(),
        required=True, allow_null=False)
    sales_id = serializers.PrimaryKeyRelatedField(
        source='sales', queryset=Sale.objects.all(),
        required=True, allow_null=False)
    category_id = serializers.PrimaryKeyRelatedField(
        source='category', queryset=Category.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Product
        fields = (
            'id',
            'created_at',
            'hash',
            'name',
            'short_description',
            'description',
            'user_id',
            'opinion_ids',
            'sales_id',
            'category_id',
            'variant_ids',  
        )