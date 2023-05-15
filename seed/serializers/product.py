"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Product
from app.models import Company
from app.models import Sale
from app.models import Category

class ProductSerializer(serializers.ModelSerializer):

    opinion_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='opinions', read_only=True)
    variant_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='variants', read_only=True)

    company_id = serializers.PrimaryKeyRelatedField(
        source='company', queryset=Company.objects.all(),
        required=True, allow_null=False)
    sale_id = serializers.PrimaryKeyRelatedField(
        source='sale', queryset=Sale.objects.all(),
        required=False, allow_null=True)
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
            'sku',
            'description',
            'company_id',
            'opinion_ids',
            'sale_id',
            'category_id',
            'variant_ids',  
        )