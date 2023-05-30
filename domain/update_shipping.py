from app.models import Shipping

def update_info_shipping(shipping_id,info):
    shipping = Shipping.objects.get(id=shipping_id)
    shipping.info = info
    shipping.save()