from app.models import Sale, Product

def change_value(saleId):
    sale = Sale.objects.get(id=saleId)
    products = Product.objects.filter(sale_id = saleId)
    for product in products:
        product.sale_id = None
        product.save()
    sale.delete()