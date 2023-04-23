"""
__Seed builder__
  AUTO_GENERATED Proxy (Read only)
  Modify via builder
"""

def get_cart():
    import seed.models.cart as SeedModel
    return SeedModel.Cart

def get_category():
    import seed.models.category as SeedModel
    return SeedModel.Category

def get_company():
    import seed.models.company as SeedModel
    return SeedModel.Company

def get_message():
    import seed.models.message as SeedModel
    return SeedModel.Message

def get_opinion():
    import seed.models.opinion as SeedModel
    return SeedModel.Opinion

def get_payment():
    import seed.models.payment as SeedModel
    return SeedModel.Payment

def get_product():
    import seed.models.product as SeedModel
    return SeedModel.Product

def get_purchase():
    import seed.models.purchase as SeedModel
    return SeedModel.Purchase

def get_sale():
    import seed.models.sale as SeedModel
    return SeedModel.Sale

def get_shipping():
    import seed.models.shipping as SeedModel
    return SeedModel.Shipping

def get_user():
    import seed.models.user as SeedModel
    return SeedModel.User

def get_variant():
    import seed.models.variant as SeedModel
    return SeedModel.Variant

def get_variantoption():
    import seed.models.variantoption as SeedModel
    return SeedModel.Variantoption

def get_file():
    import seed.models.file as SeedFile
    return SeedFile.File

Cart = get_cart()
Category = get_category()
Company = get_company()
Message = get_message()
Opinion = get_opinion()
Payment = get_payment()
Product = get_product()
Purchase = get_purchase()
Sale = get_sale()
Shipping = get_shipping()
User = get_user()
Variant = get_variant()
Variantoption = get_variantoption()
File = get_file()