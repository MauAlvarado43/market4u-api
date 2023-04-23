"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Variantoption
from app.models import Variant
from app.models import File
from seed.serializers.file import FileSerializer

class VariantoptionSerializer(serializers.ModelSerializer):
    
    photos = FileSerializer(many=True, read_only=True)

    photo_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='photos', read_only=True)

    variant_id = serializers.PrimaryKeyRelatedField(
        source='variant', queryset=Variant.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Variantoption
        fields = (
            'id',
            'created_at',
            'hash',
            'name',
            'stock',
            'photos',
            'photo_ids',
            'variant_id',  
        )