"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Cart
from app.models import User
from seed.schema.types import Cart as CartType

class SaveCartMutation(graphene.Mutation):
    
    cart = graphene.Field(CartType)
    
    class Arguments:
        payment = graphene.String(required=True)
        buyer = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        cart = {}
        if "payment" in kwargs:
            cart["payment"] = kwargs["payment"]
        if "buyer" in kwargs:
            buyer = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["buyer"])
            cart["buyer"] = buyer
        cart = \
            Cart.objects.create(**cart)
        cart.save()
    
        return SaveCartMutation(
            cart=cart)

class SetCartMutation(graphene.Mutation):
    
    cart = graphene.Field(CartType)
    
    class Arguments:
        id = graphene.Int(required=True)
        payment = graphene.String(required=False)
        buyer = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        cart = Cart.filter_permissions(
            Cart.objects,
            Cart.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "payment" in kwargs:
            cart.payment = kwargs["payment"]
        if "buyer" in kwargs:
            buyer = User.objects \
                .get(pk=kwargs["buyer"])
            cart.buyer = buyer
        cart.save()
    
        return SetCartMutation(
            cart=cart)

class DeleteCartMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        cart_id = kwargs["id"]
        cart = Cart.objects.get(pk=kwargs["id"])
        cart.delete()
        return DeleteCartMutation(
            id=cart_id)