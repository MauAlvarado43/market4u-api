from django.db.models import Q
from app.models import Product, Category
from app.serializers import SaleSerializer, FileSerializer
import openai
import json
import os

def extract_features(sentence):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    categories = Category.objects.all()
    categories = [category.name for category in categories]
    categories = ", ".join(categories)

    prompt = (
        "Extrae las siguientes características en formato JSON (category[string], name[string], brand[string], price_start[float], price_end[float], variations[JSON Array, key, value]). " 
        + "Generaliza las categorías (producto no es categoría). "
        + "No agregues información que no esté en el texto. "
        + "El nombre del producto debe ser en singular. "
        + "En caso de no haber algún atributo, pon null. "
        + "Todo en español. "
        + "En caso de que el texto solo tenga el nomrbre de una marca, category y name son null. "
        + "Las categorías disponibles son " + categories
        + "\n\n"
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt + sentence + "\n",
        temperature=0,
        max_tokens=2500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    try:
        res = response["choices"][0]["text"]
        data = json.loads(res)
    except:
        data = None
    
    return data

def get_products(sentence):

    features = extract_features(sentence)
    if features is None: return []

    category = features["category"] if features["category"] is not None else ""
    name = features["name"] if features["name"] is not None else ""
    brand = features["brand"] if features["brand"] is not None else ""
    price_start = features["price_start"] if features["price_start"] is not None else 0
    price_end = features["price_end"] if features["price_end"] is not None else 1000000
    variations = features["variations"] if features["variations"] is not None else []

    temp_variations = []
    for variant in variations:
        if variant["key"] is not None and variant["value"] is not None:
            temp_variations.append(variant)

    variations = temp_variations

    if category == name: name = ""
    for variant in variations:
        if variant["key"] in name or variant["value"] in name: name = ""

    products = Product.objects.filter(
        Q(category__name__icontains=category, name__icontains=name, company__common_name__icontains=brand) | 
        Q(category__name__icontains=category, name__icontains=name, company__name__icontains=brand)
    )
    
    response = []
    appended = {}

    if len(variations) > 0:

        for product in products:

            if product.id in appended: continue
            appended[product.id] = True

            temp_product = {
                "id": product.id,
                "sku": product.sku,
                "name": product.name,
                "short_description": product.short_description,
                "description": product.description,
                "category": product.category.name,
                "company": product.company.name,
                "sale": SaleSerializer(product.sale).data if product.sale is not None else None,
                "variants": []
            }

            for variant in product.variants.all():

                if variant.stock <= 0: continue

                for variation_requested in variations:
                        
                    if variant.price < price_start or variant.price > price_end: continue

                    found = False
                    requested_options = []

                    for option in variant.variantoptions.all():
                        requested_options.append({ "key": option.title, "value": option.value })
                        if variation_requested["key"].lower() in option.title.lower() and variation_requested["value"].lower() in option.value.lower():
                            found = True

                    if found:
                        temp_product["variants"].append({
                            "price": variant.price,
                            "stock": variant.stock,
                            "photos": FileSerializer(variant.photos, many=True).data,
                            "options": requested_options
                        })
                        break

            if len(temp_product["variants"]) > 0: 
                response.append(temp_product)

    else:

        for product in products:

            if product.id in appended: continue
            appended[product.id] = True

            temp_product = {
                "id": product.id,
                "sku": product.sku,
                "name": product.name,
                "short_description": product.short_description,
                "description": product.description,
                "category": product.category.name,
                "company": product.company.name,
                "sale": SaleSerializer(product.sale).data if product.sale is not None else None,
                "variants": []
            }

            for variant in product.variants.all():

                if variant.price < price_start or variant.price > price_end: continue
                
                options = []
                
                for option in variant.variantoptions.all():
                    options.append({ "key": option.title, "value": option.value })
                
                temp_product["variants"].append({
                    "price": variant.price,
                    "stock": variant.stock,
                    "photos": FileSerializer(variant.photos, many=True).data,
                    "options": options
                })

            if len(temp_product["variants"]) > 0: 
                response.append(temp_product)

    response = response[-5:]

    return response