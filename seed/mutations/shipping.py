"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Shipping
from app.models import Cart
from app.models import User
from app.models import Company
from seed.schema.types import Shipping as ShippingType

class SaveShippingMutation(graphene.Mutation):
    
    shipping = graphene.Field(ShippingType)
    
    class Arguments:
        info = graphene.String(required=True)
        folio = graphene.String(required=True)
        address = graphene.String(required=True)
        status = graphene.String(required=True)
        total = graphene.Float(required=True)
        subtotal = graphene.Float(required=True)
        shipment = graphene.Float(required=True)
        cart = graphene.Int(required=True)
        buyer = graphene.Int(required=False)
        company = graphene.Int(required=False)
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
        if "total" in kwargs:
            shipping["total"] = kwargs["total"]
        if "subtotal" in kwargs:
            shipping["subtotal"] = kwargs["subtotal"]
        if "shipment" in kwargs:
            shipping["shipment"] = kwargs["shipment"]
        if "cart" in kwargs:
            cart = Cart.filter_permissions(
                Cart.objects,
                Cart.permission_filters(user)) \
                .get(pk=kwargs["cart"])
            shipping["cart"] = cart
        if "buyer" in kwargs:
            buyer = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["buyer"])
            shipping["buyer"] = buyer
        if "company" in kwargs:
            company = Company.filter_permissions(
                Company.objects,
                Company.permission_filters(user)) \
                .get(pk=kwargs["company"])
            shipping["company"] = company
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
        total = graphene.Float(required=False)
        subtotal = graphene.Float(required=False)
        shipment = graphene.Float(required=False)
        cart = graphene.Int(required=False)
        buyer = graphene.Int(required=False)
        company = graphene.Int(required=False)
        
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
        if "total" in kwargs:
            shipping.total = kwargs["total"]
        if "subtotal" in kwargs:
            shipping.subtotal = kwargs["subtotal"]
        if "shipment" in kwargs:
            shipping.shipment = kwargs["shipment"]
        if "cart" in kwargs:
            cart = Cart.objects \
                .get(pk=kwargs["cart"])
            shipping.cart = cart
        if "buyer" in kwargs:
            buyer = User.objects \
                .get(pk=kwargs["buyer"])
            shipping.buyer = buyer
        if "company" in kwargs:
            company = Company.objects \
                .get(pk=kwargs["company"])
            shipping.company = company
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