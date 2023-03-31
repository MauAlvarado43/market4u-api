"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Category

class CategorySerializer(serializers.ModelSerializer):

    product_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='products', read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'created_at',
            'hash',
            'name',
            'product_ids',  
        )