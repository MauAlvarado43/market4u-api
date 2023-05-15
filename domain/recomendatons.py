import random
import json
import pandas as pd
from pyECLAT import ECLAT
from app.models import Purchase, Cart, Product, User, Payment, Shipping
from app.serializers import ProductSerializer

def generate_recomendations():

    transactions = []

    carts = Cart.objects.all()
    for cart in carts:

        purchased_products = []

        shippings = cart.shippings.all()
        for shipping in shippings:

            purchases = shipping.purchases.all()
            for purchase in purchases:

                product = purchase.product
                purchased_products.append("xxxxx" + str(product['id']) + "xxxxx")

        if len(purchased_products) > 0: 
            transactions.append(purchased_products)
    
    min_n_products = 2
    min_support = 7 / len(transactions)
    max_length = max([len(x) for x in transactions])

    df = pd.DataFrame(transactions)
    eclat = ECLAT(df, verbose = True)
    rule_indexes, rule_supports = eclat.fit(min_support=min_support, min_combination=min_n_products, max_combination=max_length, separator="&", verbose=True)

    related_products = {}

    for rule in rule_supports:

        items = rule.split("&")
        if len(items) < 2: continue

        cleaned_items = []

        for item in items:
            item = item.replace("xxxxx", "")
            item = item.replace("xxxxx", "")
            item = int(item)
            cleaned_items.append(item)

        for item in cleaned_items:

            if item not in related_products:
                related_products[item] = []

            for item2 in cleaned_items:
                if item2 != item and item2 not in related_products[item]:
                    related_products[item].append(item2)

    with open('./domain/models/related_products.json', 'w') as fp:
        json.dump(related_products, fp)

def get_related_products(product_id):

    try:
        with open('./domain/models/related_products.json') as json_file:
            related_products = json.load(json_file)
    except:
        related_products = {}

    product = Product.objects.get(id = product_id)

    if str(product_id) in related_products:
        ids = related_products[str(product_id)]
        products = Product.objects.filter(id__in = ids)
    else:
        products = Product.objects.filter(category = product.category)

    response_products = []

    for product in products:
        response_products.append({
            "id": product.id,
            "name": product.name,
            "shortDescription": product.short_description,
            "variants": [ 
                {
                    "price": variant.price,
                    "photos": [ 
                        {
                            "id": photo.id,
                            "url": photo.url
                        } for photo in variant.photos.all() 
                    ]
                } for variant in product.variants.all() 
            ],
            "opinions": [
                {
                    "title": opinion.title,
                    "description": opinion.description,
                    "rate": opinion.rate,
                    "user": {
                        "id": opinion.user.id,
                    }
                } for opinion in product.opinions.all()
            ],
        })

    return response_products

def generate_purchases(n):

    for i in range(n):

        users = User.objects.all()
        payments = Payment.objects.all()
        products = Product.objects.all()

        for user in users:
            for payment in payments:

                cart = Cart.objects.create(buyer=user, payment=payment)
                shipping = Shipping.objects.create(cart=cart, status="CREATED", seller=user, info="", folio="", address="")
                temp_products = products

                for i in range(0, random.randint(1, 10) + 1):
                    product = random.choice(temp_products)
                    temp_products = temp_products.exclude(id=product.id)
                    Purchase.objects.create(shipping=shipping, product=ProductSerializer(product).data, amount=random.randint(1, 5))