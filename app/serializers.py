"""
__Seed builder__
  AUTO_GENERATED Proxy (Read only)
  Modify via builder
"""

def get_cart_serializer():
    import seed.serializers.cart as SeedSerializer
    return SeedSerializer.CartSerializer

def get_category_serializer():
    import seed.serializers.category as SeedSerializer
    return SeedSerializer.CategorySerializer

def get_company_serializer():
    import seed.serializers.company as SeedSerializer
    return SeedSerializer.CompanySerializer

def get_message_serializer():
    import seed.serializers.message as SeedSerializer
    return SeedSerializer.MessageSerializer

def get_opinion_serializer():
    import seed.serializers.opinion as SeedSerializer
    return SeedSerializer.OpinionSerializer

def get_payment_serializer():
    import seed.serializers.payment as SeedSerializer
    return SeedSerializer.PaymentSerializer

def get_product_serializer():
    import seed.serializers.product as SeedSerializer
    return SeedSerializer.ProductSerializer

def get_purchase_serializer():
    import seed.serializers.purchase as SeedSerializer
    return SeedSerializer.PurchaseSerializer

def get_sale_serializer():
    import seed.serializers.sale as SeedSerializer
    return SeedSerializer.SaleSerializer

def get_user_serializer():
    import seed.serializers.user as SeedSerializer
    return SeedSerializer.UserSerializer

def get_file_serializer():
    import seed.serializers.file as SeedSerializer
    return SeedSerializer.FileSerializer

CartSerializer = get_cart_serializer()
CategorySerializer = get_category_serializer()
CompanySerializer = get_company_serializer()
MessageSerializer = get_message_serializer()
OpinionSerializer = get_opinion_serializer()
PaymentSerializer = get_payment_serializer()
ProductSerializer = get_product_serializer()
PurchaseSerializer = get_purchase_serializer()
SaleSerializer = get_sale_serializer()
UserSerializer = get_user_serializer()
FileSerializer = get_file_serializer()