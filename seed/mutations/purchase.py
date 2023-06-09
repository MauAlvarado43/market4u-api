"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Purchase
from app.models import Shipping
from graphene.types.generic import GenericScalar
from seed.schema.types import Purchase as PurchaseType

class SavePurchaseMutation(graphene.Mutation):
    
    purchase = graphene.Field(PurchaseType)
    
    class Arguments:
        amount = graphene.Int(required=True)
        product = GenericScalar(required=True)
        sale = GenericScalar(required=True)
        shipping = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        purchase = {}
        if "amount" in kwargs:
            purchase["amount"] = kwargs["amount"]
        if "product" in kwargs:
            purchase["product"] = kwargs["product"]
        if "sale" in kwargs:
            purchase["sale"] = kwargs["sale"]
        if "shipping" in kwargs:
            shipping = Shipping.filter_permissions(
                Shipping.objects,
                Shipping.permission_filters(user)) \
                .get(pk=kwargs["shipping"])
            purchase["shipping"] = shipping
        purchase = \
            Purchase.objects.create(**purchase)
        purchase.save()
    
        return SavePurchaseMutation(
            purchase=purchase)

class SetPurchaseMutation(graphene.Mutation):
    
    purchase = graphene.Field(PurchaseType)
    
    class Arguments:
        id = graphene.Int(required=True)
        amount = graphene.Int(required=False)
        product = GenericScalar(required=False)
        sale = GenericScalar(required=False)
        shipping = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        purchase = Purchase.filter_permissions(
            Purchase.objects,
            Purchase.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "amount" in kwargs:
            purchase.amount = kwargs["amount"]
        if "product" in kwargs:
            purchase.product = kwargs["product"]
        if "sale" in kwargs:
            purchase.sale = kwargs["sale"]
        if "shipping" in kwargs:
            shipping = Shipping.objects \
                .get(pk=kwargs["shipping"])
            purchase.shipping = shipping
        purchase.save()
    
        return SetPurchaseMutation(
            purchase=purchase)

class DeletePurchaseMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        purchase_id = kwargs["id"]
        purchase = Purchase.objects.get(pk=kwargs["id"])
        purchase.delete()
        return DeletePurchaseMutation(
            id=purchase_id)