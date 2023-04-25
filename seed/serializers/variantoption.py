"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Variantoption
from app.models import Variant

class VariantoptionSerializer(serializers.ModelSerializer):

    variant_id = serializers.PrimaryKeyRelatedField(
        source='variant', queryset=Variant.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Variantoption
        fields = (
            'id',
            'created_at',
            'hash',
            'title',
            'value',
            'variant_id',  
        )