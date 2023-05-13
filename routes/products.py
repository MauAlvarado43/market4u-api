"""
__Seed builder__
  Extended module
"""

import seed.routes.products as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from app.models import Product, User, Category, Sale, Variant, Variantoption, File
from app.serializers import ProductSerializer
from domain.save_variants import save_variants

from domain.update_info_product import update_info_null_product
from domain.nullable_products import change_value

class ProductViewSet(SeedRoute.ProductViewSet):
    
    @action(detail = False, methods = ['POST'])
    def create_product(self, request):
        
        has_fields_or_400(request.data, 'user', 'name', 'short_description', 'description', 'category')

        user = get_object_or_404(User, pk = request.data['user'])
        category = get_object_or_404(Category, pk = request.data['category'])
        company = user.company

        product = Product.objects.create(
            name = request.data['name'],
            short_description = request.data['short_description'],
            description = request.data['description'],
            company = company,
            category = category
        )
        product.save()

        if 'sale' in request.data:
            sale = get_object_or_404(Sale, pk = request.data['sale'])
            product.sale = sale
            product.save()

        response = save_variants(request, product)
        return response
    
    @action(methods = ['POST'], detail = False)
    def update_product(self, request):

        has_fields_or_400(request.data, 'name', 'short_description', 'description', 'category', 'product', 'user', 'product')

        user = get_object_or_404(User, pk = request.data['user'])
        category = get_object_or_404(Category, pk = request.data['category'])
        product = get_object_or_404(Product, pk = request.data['product'])

        if product.company.id != user.company.id:
            return Response(status = status.HTTP_401_UNAUTHORIZED)
        
        product.name = request.data['name']
        product.short_description = request.data['short_description']
        product.description = request.data['description']
        product.category = category
        product.save()

        if 'sale' in request.data:
            sale = get_object_or_404(Sale, pk = request.data['sale'])
            product.sale = sale
            product.save()

        for variant in product.variants.all(): variant.delete()
        response = save_variants(request, product)
        return response
    
    @action(detail=False, methods=['POST'])
    def update_product_null(self,request):
        data = request.data
        print(data)
        has_fields_or_400(data,'product_id')
        update_info_null_product(data['product_id'])
        return Response(status=status.HTTP_200_OK)
    ########
    @action(detail=False, methods=["POST"])
    def nullable_products(self,request):
        data = request.data 
        print(data)
        has_fields_or_400(data,'sale_id')
        change_value(data['sale_id'])
        return Response(status=status.HTTP_200_OK)