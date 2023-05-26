"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.models import Cart
from app.models import Category
from app.models import Company
from app.models import Message
from app.models import Opinion
from app.models import Payment
from app.models import Product
from app.models import Purchase
from app.models import Sale
from app.models import Shipping
from app.models import User
from app.models import Variant
from app.models import Variantoption
from app.models import File

class Admin:
    # pylint: disable=R0914,R0915
    @staticmethod
    def register():
        
        class CartResource(resources.ModelResource):
            pass

        class CartAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = CartResource
            class Meta:
                model = Cart
                fields = (
                    'id',
                    'created_at',
                    'buyer',
                    'payment',
                    'shippings',
                )
        
        class CategoryResource(resources.ModelResource):
            pass

        class CategoryAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = CategoryResource
            class Meta:
                model = Category
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'products',
                )
        
        class CompanyResource(resources.ModelResource):
            pass

        class CompanyAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = CompanyResource
            class Meta:
                model = Company
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'common_name',
                    'rfc',
                    'cp',
                    'phone',
                    'email',
                    'active',
                    'photo',
                    'municipality',
                    'state',
                    'cologn',
                    'website',
                    'street',
                    'city',
                    'photo',
                    'users',
                )
        
        class MessageResource(resources.ModelResource):
            pass

        class MessageAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = MessageResource
            class Meta:
                model = Message
                fields = (
                    'id',
                    'created_at',
                    'content',
                    'sender',
                    'target',
                )
        
        class OpinionResource(resources.ModelResource):
            pass

        class OpinionAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = OpinionResource
            class Meta:
                model = Opinion
                fields = (
                    'id',
                    'created_at',
                    'title',
                    'description',
                    'rate',
                    'product',
                    'user',
                )
        
        class PaymentResource(resources.ModelResource):
            pass

        class PaymentAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = PaymentResource
            class Meta:
                model = Payment
                fields = (
                    'id',
                    'created_at',
                    'card_number',
                    'expire_date',
                    'type',
                    'address',
                    'bank',
                    'name',
                    'user',
                )
        
        class ProductResource(resources.ModelResource):
            pass

        class ProductAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = ProductResource
            class Meta:
                model = Product
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'short_description',
                    'sku',
                    'description',
                    'company',
                    'opinions',
                    'sale',
                    'category',
                    'variants',
                )
        
        class PurchaseResource(resources.ModelResource):
            pass

        class PurchaseAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = PurchaseResource
            class Meta:
                model = Purchase
                fields = (
                    'id',
                    'created_at',
                    'amount',
                    'product',
                    'sale',
                    'shipping',
                )
        
        class SaleResource(resources.ModelResource):
            pass

        class SaleAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = SaleResource
            class Meta:
                model = Sale
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'disscount',
                    'start_date',
                    'end_date',
                    'banner',
                    'banner',
                    'product',
                    'company',
                )
        
        class ShippingResource(resources.ModelResource):
            pass

        class ShippingAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = ShippingResource
            class Meta:
                model = Shipping
                fields = (
                    'id',
                    'created_at',
                    'info',
                    'folio',
                    'address',
                    'status',
                    'seller',
                    'cart',
                )
        
        class UserResource(resources.ModelResource):
            pass

        class UserAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = UserResource
            class Meta:
                model = User
                fields = (
                    'id',
                    'created_at',
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
                    'photo',
                    'company',
                    'carts',
                    'wishlist',
                    'shippings',
                )
        
        class VariantResource(resources.ModelResource):
            pass

        class VariantAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = VariantResource
            class Meta:
                model = Variant
                fields = (
                    'id',
                    'created_at',
                    'price',
                    'stock',
                    'photos',
                    'shipment',
                    'photos',
                    'options',
                    'product',
                )
        
        class VariantoptionResource(resources.ModelResource):
            pass

        class VariantoptionAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = VariantoptionResource
            class Meta:
                model = Variantoption
                fields = (
                    'id',
                    'created_at',
                    'title',
                    'value',
                    'variant',
                )
        
        class FileResource(resources.ModelResource):
            pass

        class FileAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
            resource_class = FileResource
            class Meta:
                model = File
                fields = (
                    'id',
                    'created_at',
                    'name',
                    'url',
                    'size'
                )
        admin.site.register(Cart, CartAdmin)
        admin.site.register(Category, CategoryAdmin)
        admin.site.register(Company, CompanyAdmin)
        admin.site.register(Message, MessageAdmin)
        admin.site.register(Opinion, OpinionAdmin)
        admin.site.register(Payment, PaymentAdmin)
        admin.site.register(Product, ProductAdmin)
        admin.site.register(Purchase, PurchaseAdmin)
        admin.site.register(Sale, SaleAdmin)
        admin.site.register(Shipping, ShippingAdmin)
        admin.site.register(User, UserAdmin)
        admin.site.register(Variant, VariantAdmin)
        admin.site.register(Variantoption, VariantoptionAdmin)
        admin.site.register(File, FileAdmin)