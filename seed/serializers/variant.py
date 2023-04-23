"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Variant
from app.models import Product

class VariantSerializer(serializers.ModelSerializer):

    option_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='variantoptions', read_only=True)

    product_id = serializers.PrimaryKeyRelatedField(
        source='product', queryset=Product.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Variant
        fields = (
            'id',
            'created_at',
            'hash',
            'name',
            'option_ids',
            'product_id',  
        )