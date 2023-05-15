"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Product
from app.models import Company
from app.models import Sale
from app.models import Category
from seed.schema.types import Product as ProductType

class SaveProductMutation(graphene.Mutation):
    
    product = graphene.Field(ProductType)
    
    class Arguments:
        name = graphene.String(required=True)
        shortDescription = graphene.String(required=True)
        sku = graphene.String(required=True)
        description = graphene.String(required=True)
        company = graphene.Int(required=True)
        sale = graphene.Int(required=False)
        category = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        product = {}
        if "name" in kwargs:
            product["name"] = kwargs["name"]
        if "shortDescription" in kwargs:
            product["short_description"] = kwargs["shortDescription"]
        if "sku" in kwargs:
            product["sku"] = kwargs["sku"]
        if "description" in kwargs:
            product["description"] = kwargs["description"]
        if "company" in kwargs:
            company = Company.filter_permissions(
                Company.objects,
                Company.permission_filters(user)) \
                .get(pk=kwargs["company"])
            product["company"] = company
        if "sale" in kwargs:
            sale = Sale.filter_permissions(
                Sale.objects,
                Sale.permission_filters(user)) \
                .get(pk=kwargs["sale"])
            product["sale"] = sale
        if "category" in kwargs:
            category = Category.filter_permissions(
                Category.objects,
                Category.permission_filters(user)) \
                .get(pk=kwargs["category"])
            product["category"] = category
        product = \
            Product.objects.create(**product)
        product.save()
    
        return SaveProductMutation(
            product=product)

class SetProductMutation(graphene.Mutation):
    
    product = graphene.Field(ProductType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        shortDescription = graphene.String(required=False)
        sku = graphene.String(required=False)
        description = graphene.String(required=False)
        company = graphene.Int(required=False)
        sale = graphene.Int(required=False)
        category = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        product = Product.filter_permissions(
            Product.objects,
            Product.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "name" in kwargs:
            product.name = kwargs["name"]
        if "shortDescription" in kwargs:
            product.short_description = kwargs["shortDescription"]
        if "sku" in kwargs:
            product.sku = kwargs["sku"]
        if "description" in kwargs:
            product.description = kwargs["description"]
        if "company" in kwargs:
            company = Company.objects \
                .get(pk=kwargs["company"])
            product.company = company
        if "sale" in kwargs:
            sale = Sale.objects \
                .get(pk=kwargs["sale"])
            product.sale = sale
        if "category" in kwargs:
            category = Category.objects \
                .get(pk=kwargs["category"])
            product.category = category
        product.save()
    
        return SetProductMutation(
            product=product)

class DeleteProductMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        product_id = kwargs["id"]
        product = Product.objects.get(pk=kwargs["id"])
        product.delete()
        return DeleteProductMutation(
            id=product_id)