"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import User
from app.models import Company
from app.models import File
from seed.serializers.file import FileSerializer

class UserSerializer(serializers.ModelSerializer):
    
    photo = FileSerializer(read_only=True)

    cart_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='buyer_carts', read_only=True)
    product_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='products', read_only=True)
    whishlist_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='products', read_only=True)
    sale_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='sales', read_only=True)
    shipping_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='seller_shippings', read_only=True)

    company_id = serializers.PrimaryKeyRelatedField(
        source='company', queryset=Company.objects.all(),
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
            'address',
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
            'born_date',
            'photo_id',
            'company_id',
            'cart_ids',
            'product_ids',
            'whishlist_ids',
            'sale_ids',
            'shipping_ids',  
        )