"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import User
from app.models import Company
from app.models import Product
from app.models import File
from seed.serializers.file import FileSerializer

class UserSerializer(serializers.ModelSerializer):
    
    photo = FileSerializer(read_only=True)

    cart_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='buyer_carts', read_only=True)
    shipping_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='seller_shippings', read_only=True)

    company_id = serializers.PrimaryKeyRelatedField(
        source='company', queryset=Company.objects.all(),
        required=False, allow_null=True)
    wishlist_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='wishlist', queryset=Product.objects.all(),
        required=False, allow_null=True)
    photo_id = serializers.PrimaryKeyRelatedField(
        source='photo', queryset=File.objects.all(),
        required=False, allow_null=True)

    class Meta:
        model = User
        fields = (
            'id',
            'created_at',
            'hash',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'active',
            'photo',
            'type',
            'street',
            'city',
            'cp',
            'municipality',
            'state',
            'cologn',
            'telephone',
            'token',
            'token_verified',
            'code',
            'photo_id',
            'company_id',
            'cart_ids',
            'wishlist_ids',
            'shipping_ids',  
        )