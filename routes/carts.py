"""
__Seed builder__
  Extended module
"""

import seed.routes.carts as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.models import Cart
from app.serializers import ProductSerializer, VariantSerializer, CategorySerializer
from app.models import Product, Variant, Category
from domain.cart.create_purchase import create_purchase

class CartViewSet(SeedRoute.CartViewSet):
    
    @action(detail=False, methods=["POST"])
    def active_products(self, request): 
        data = request.data
        has_fields_or_400(data, "cart")
        cart = data["cart"]

        response = []
        for item in cart:
            product_id = item["product"]
            vartian_id = item["variant"]
            amount = item["amount"]

            product = Product.objects.get(pk=product_id)
            variant = Variant.objects.get(pk=vartian_id)

            serializer_products = ProductSerializer(product, many=False)
            serializer_variants = VariantSerializer(variant, many=False)
            serializer_category = CategorySerializer(product.category, many=False)

            response.append({**serializer_products.data, "category": serializer_category.data, "variant": serializer_variants.data, "amount": amount})

        return Response(status=200, data=response)
    
    @action(detail=False, methods=["POST"])
    def purchase(self, request): 
        data = request.data
        has_fields_or_400(data, "products", "delivery", "payment", "user")
        products = data["products"]
        delivery = data["delivery"]
        payment = data["payment"]
        user = data["user"]

        response, message = create_purchase(user, products, delivery, payment)
        return Response(status=response, data=message)
