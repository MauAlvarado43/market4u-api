"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Shipping
from app.models import User
from app.models import Cart
from seed.schema.types import Shipping as ShippingType

class SaveShippingMutation(graphene.Mutation):
    
    shipping = graphene.Field(ShippingType)
    
    class Arguments:
        info = graphene.String(required=True)
        folio = graphene.String(required=True)
        address = graphene.String(required=True)
        status = graphene.String(required=True)
        seller = graphene.Int(required=True)
        cart = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        shipping = {}
        if "info" in kwargs:
            shipping["info"] = kwargs["info"]
        if "folio" in kwargs:
            shipping["folio"] = kwargs["folio"]
        if "address" in kwargs:
            shipping["address"] = kwargs["address"]
        if "status" in kwargs:
            shipping["status"] = kwargs["status"]
        if "seller" in kwargs:
            seller = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["seller"])
            shipping["seller"] = seller
        if "cart" in kwargs:
            cart = Cart.filter_permissions(
                Cart.objects,
                Cart.permission_filters(user)) \
                .get(pk=kwargs["cart"])
            shipping["cart"] = cart
        shipping = \
            Shipping.objects.create(**shipping)
        shipping.save()
    
        return SaveShippingMutation(
            shipping=shipping)

class SetShippingMutation(graphene.Mutation):
    
    shipping = graphene.Field(ShippingType)
    
    class Arguments:
        id = graphene.Int(required=True)
        info = graphene.String(required=False)
        folio = graphene.String(required=False)
        address = graphene.String(required=False)
        status = graphene.String(required=False)
        seller = graphene.Int(required=False)
        cart = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        shipping = Shipping.filter_permissions(
            Shipping.objects,
            Shipping.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "info" in kwargs:
            shipping.info = kwargs["info"]
        if "folio" in kwargs:
            shipping.folio = kwargs["folio"]
        if "address" in kwargs:
            shipping.address = kwargs["address"]
        if "status" in kwargs:
            shipping.status = kwargs["status"]
        if "seller" in kwargs:
            seller = User.objects \
                .get(pk=kwargs["seller"])
            shipping.seller = seller
        if "cart" in kwargs:
            cart = Cart.objects \
                .get(pk=kwargs["cart"])
            shipping.cart = cart
        shipping.save()
    
        return SetShippingMutation(
            shipping=shipping)

class DeleteShippingMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        shipping_id = kwargs["id"]
        shipping = Shipping.objects.get(pk=kwargs["id"])
        shipping.delete()
        return DeleteShippingMutation(
            id=shipping_id)