"""
__Seed builder__
  AUTO_GENERATED Proxy (Read only)
  Modify via builder
"""

def get_cart_viewset():
    import seed.routes.carts as SeedViewSet
    return SeedViewSet.CartViewSet

def get_category_viewset():
    import seed.routes.categories as SeedViewSet
    return SeedViewSet.CategoryViewSet

def get_company_viewset():
    import seed.routes.companies as SeedViewSet
    return SeedViewSet.CompanyViewSet

def get_message_viewset():
    import seed.routes.messages as SeedViewSet
    return SeedViewSet.MessageViewSet

def get_opinion_viewset():
    import seed.routes.opinions as SeedViewSet
    return SeedViewSet.OpinionViewSet

def get_payment_viewset():
    import seed.routes.payments as SeedViewSet
    return SeedViewSet.PaymentViewSet

def get_product_viewset():
    import seed.routes.products as SeedViewSet
    return SeedViewSet.ProductViewSet

def get_purchase_viewset():
    import seed.routes.purchases as SeedViewSet
    return SeedViewSet.PurchaseViewSet

def get_sale_viewset():
    import seed.routes.sales as SeedViewSet
    return SeedViewSet.SaleViewSet

def get_user_viewset():
    import seed.routes.users as SeedViewSet
    return SeedViewSet.UserViewSet

def get_file_view():
    import seed.routes.files as SeedView
    return SeedView.FileView

CartViewSet = get_cart_viewset()
CategoryViewSet = get_category_viewset()
CompanyViewSet = get_company_viewset()
MessageViewSet = get_message_viewset()
OpinionViewSet = get_opinion_viewset()
PaymentViewSet = get_payment_viewset()
ProductViewSet = get_product_viewset()
PurchaseViewSet = get_purchase_viewset()
SaleViewSet = get_sale_viewset()
UserViewSet = get_user_viewset()
FileView = get_file_view()