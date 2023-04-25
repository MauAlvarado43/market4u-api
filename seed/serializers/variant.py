"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Variant
from app.models import Product
from app.models import File
from seed.serializers.file import FileSerializer

class VariantSerializer(serializers.ModelSerializer):
    
    photos = FileSerializer(many=True, read_only=True)

    option_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='variantoptions', read_only=True)
    photo_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='photos', read_only=True)

    product_id = serializers.PrimaryKeyRelatedField(
        source='product', queryset=Product.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Variant
        fields = (
            'id',
            'created_at',
            'hash',
            'price',
            'stock',
            'photos',
            'photo_ids',
            'option_ids',
            'product_id',  
        )