"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Variant
from app.models import Product
from seed.schema.types import Variant as VariantType

class SaveVariantMutation(graphene.Mutation):
    
    variant = graphene.Field(VariantType)
    
    class Arguments:
        name = graphene.String(required=True)
        product = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        variant = {}
        if "name" in kwargs:
            variant["name"] = kwargs["name"]
        if "product" in kwargs:
            product = Product.filter_permissions(
                Product.objects,
                Product.permission_filters(user)) \
                .get(pk=kwargs["product"])
            variant["product"] = product
        variant = \
            Variant.objects.create(**variant)
        variant.save()
    
        return SaveVariantMutation(
            variant=variant)

class SetVariantMutation(graphene.Mutation):
    
    variant = graphene.Field(VariantType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        product = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        variant = Variant.filter_permissions(
            Variant.objects,
            Variant.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "name" in kwargs:
            variant.name = kwargs["name"]
        if "product" in kwargs:
            product = Product.objects \
                .get(pk=kwargs["product"])
            variant.product = product
        variant.save()
    
        return SetVariantMutation(
            variant=variant)

class DeleteVariantMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        variant_id = kwargs["id"]
        variant = Variant.objects.get(pk=kwargs["id"])
        variant.delete()
        return DeleteVariantMutation(
            id=variant_id)