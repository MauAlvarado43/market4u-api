import json
from django.utils.crypto import get_random_string
from app.serializers import ProductSerializer, VariantSerializer, CategorySerializer, SaleSerializer, VariantoptionSerializer
from app.models import Shipping, Purchase, Cart, User, Product, Variant, Payment, Company, Sale, Variantoption

def create_purchase(user_id, products = [], delivery = {}, payment_raw = {}):

    for product in products:
        if not validate_stock(product):
            return 200, product["sku"] 

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

    if delivery["save"]:
        user.telephone = delivery["telephone"]
        user.street = delivery["street"]
        user.cologn = delivery["cologn"]
        user.cp = delivery["cp"]
        user.city = delivery["city"]
        user.state = delivery["state"]
        user.save()

    save_products(user, cart, delivery, products)
    return 201, None


def save_products(user, cart, delivery, products):

    companies = []

    for product in products:
        if product["company_id"] not in companies:
            companies.append(product["company_id"])

    for company_id in companies:
        products_company = get_products_by_company(products, company_id)
        company = Company.objects.get(id=company_id)
        folio = get_random_string(length=15)

        shipping = Shipping.objects.create(
            info="",
            folio=folio,
            address=json.dumps(delivery, separators=(',', ':')),
            status="CREATED",
            cart=cart,
            buyer=user,
            company=company
        ) 
        total = 0
        subtotal = 0
        shipment = 0

        for product_raw in products_company:
            
            sale_raw = product_raw.get("sale")
            sale = None
            product = Product.objects.get(id=product_raw["id"])
            variant = Variant.objects.get(id=product_raw["variant"]["id"])
            variant_options = Variantoption.objects.filter(variant=variant)
            category = product.category

            product_json = {
                "product": ProductSerializer(product, many=False).data,
                "variant": VariantSerializer(variant, many=False).data,
                "variant_options": VariantoptionSerializer(variant_options, many=True).data,
                "category": CategorySerializer(category, many=False).data
            }

            if sale_raw is not None:
                sale = Sale.objects.get(id=sale_raw["id"])
                new_price = variant.price - (variant.price * (sale.disscount / 100))
                subtotal += product_raw["amount"] * new_price
                shipment += variant.shipment
            else:
                subtotal += product_raw["amount"] * variant.price
                shipment += variant.shipment
                
            remove_stock(variant.id, product_raw["amount"])

            Purchase.objects.create(
                amount=product_raw["amount"],
                product=json.dumps(product_json),
                sale="" if sale is None else SaleSerializer(sale, many=False).data,
                shipping=shipping
            )

        shipping.shipment = shipment
        shipping.subtotal = subtotal
        shipping.total = subtotal + shipment
        shipping.save()

def get_products_by_company(products, company_id):
    filtered_products = []
    for product in products:
        if product["company_id"] == company_id:
            filtered_products.append(product)

    return filtered_products

def validate_stock(product_raw):

    amount = product_raw["amount"]
    variant = Variant.objects.get(id=product_raw["variant"]["id"])

    if amount > variant.stock:
        return False
    
    return True

def remove_stock(variant_id, amount):
    variant = Variant.objects.get(id=variant_id)
    variant.stock -= amount
    variant.save()