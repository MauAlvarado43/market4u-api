from app.models import Sale, Product

def change_value(saleId):
    sale = Sale.objects.get(id=saleId)
    print(sale)
    products = Product.objects.filter(sale__id = saleId)
    for product in products:
        print(product)
        product.sale = None
        product.save()
    sale.delete()