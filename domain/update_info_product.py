from app.models import Product, Sale

def update_info_null_product(product_id):
    product = Product.objects.get(id=product_id)
    product.sale = None
    product.save()

