"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Sale
from app.models import User
from app.models import File
from seed.serializers.file import FileSerializer

class SaleSerializer(serializers.ModelSerializer):
    
    banner = FileSerializer(read_only=True)

    product_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='products', read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=User.objects.all(),
        required=True, allow_null=False)
    banner_id = serializers.PrimaryKeyRelatedField(
        source='banner', queryset=File.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Sale
        fields = (
            'id',
            'created_at',
            'hash',
            'name',
            'disscount',
            'start_date',
            'end_date',
            'banner',
            'banner_id',
            'product_ids',
            'user_id',  
        )