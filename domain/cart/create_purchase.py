import json
from django.utils.crypto import get_random_string
from app.serializers import ProductSerializer, VariantSerializer
from app.models import Shipping, Purchase, Cart, User, Product, Variant, Payment

def create_purchase(user_id, products = [], delivery = {}, payment_raw = {}):

    user = User.objects.get(id=user_id)
    cart = Cart.objects.create(
        buyer = user,
        payment = json.dumps(payment_raw)
    )
    if payment_raw["save"]:
        payment = Payment.objects.filter(card_number=payment_raw["cardNumber"])
        if payment.exists():
            pass
        else:
            Payment.objects.create(
                card_number=payment_raw["cardNumber"],
                expire_date=payment_raw["expireDate"],
                type=payment_raw["type"],
                address=payment_raw["address"],
                bank=payment_raw["bank"],
                name=payment_raw["name"],
                user=user
            )

    save_products(user, cart, delivery, products)
    return True


def save_products(user, cart, delivery, products):

    companies = []

    for product in products:
        if product["company_id"] not in companies:
            companies.append(product["company_id"])

    for company_id in companies:
        products_company = get_products_by_company(products, company_id)
        folio = get_random_string(length=15)

        shipping = Shipping.objects.create(
            info="",
            folio=folio,
            address=json.dumps(delivery),
            status="CREATED",
            cart=cart,
            buyer=user
        ) 

        for product_raw in products_company:
            
            product = Product.objects.get(id=product_raw["id"])
            variant = Variant.objects.get(id=product_raw["variant"]["id"])

            product_json = {
                "product": ProductSerializer(product, many=False).data,
                "variant": VariantSerializer(variant, many=False).data
            }

            Purchase.objects.create(
                amount=product_raw["amount"],
                product=json.dumps(product_json),
                sale="",
                shipping=shipping
            )


def get_products_by_company(products, company_id):
    filtered_products = []
    for product in products:
        if product["company_id"] == company_id:
            filtered_products.append(product)

    return filtered_products