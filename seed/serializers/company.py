"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Company
from app.models import File
from seed.serializers.file import FileSerializer

class CompanySerializer(serializers.ModelSerializer):
    
    photo = FileSerializer(read_only=True)

    user_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='users', read_only=True)

    photo_id = serializers.PrimaryKeyRelatedField(
        source='photo', queryset=File.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Company
        fields = (
            'id',
            'created_at',
            'hash',
            'name',
            'common_name',
            'rfc',
            'address',
            'phone',
            'email',
            'active',
            'photo',
            'photo_id',
            'user_ids',  
        )