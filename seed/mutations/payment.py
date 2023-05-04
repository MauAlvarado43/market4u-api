"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Payment
from app.models import User
from seed.schema.types import Payment as PaymentType

class SavePaymentMutation(graphene.Mutation):
    
    payment = graphene.Field(PaymentType)
    
    class Arguments:
        cardNumber = graphene.String(required=True)
        expireDate = graphene.String(required=True)
        type = graphene.String(required=True)
        address = graphene.String(required=True)
        bank = graphene.String(required=True)
        user = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        payment = {}
        if "cardNumber" in kwargs:
            payment["card_number"] = kwargs["cardNumber"]
        if "expireDate" in kwargs:
            payment["expire_date"] = kwargs["expireDate"]
        if "type" in kwargs:
            payment["type"] = kwargs["type"]
        if "address" in kwargs:
            payment["address"] = kwargs["address"]
        if "bank" in kwargs:
            payment["bank"] = kwargs["bank"]
        if "user" in kwargs:
            user = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["user"])
            payment["user"] = user
        payment = \
            Payment.objects.create(**payment)
        payment.save()
    
        return SavePaymentMutation(
            payment=payment)

class SetPaymentMutation(graphene.Mutation):
    
    payment = graphene.Field(PaymentType)
    
    class Arguments:
        id = graphene.Int(required=True)
        cardNumber = graphene.String(required=False)
        expireDate = graphene.String(required=False)
        type = graphene.String(required=False)
        address = graphene.String(required=False)
        bank = graphene.String(required=False)
        user = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        payment = Payment.filter_permissions(
            Payment.objects,
            Payment.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "cardNumber" in kwargs:
            payment.card_number = kwargs["cardNumber"]
        if "expireDate" in kwargs:
            payment.expire_date = kwargs["expireDate"]
        if "type" in kwargs:
            payment.type = kwargs["type"]
        if "address" in kwargs:
            payment.address = kwargs["address"]
        if "bank" in kwargs:
            payment.bank = kwargs["bank"]
        if "user" in kwargs:
            user = User.objects \
                .get(pk=kwargs["user"])
            payment.user = user
        payment.save()
    
        return SetPaymentMutation(
            payment=payment)

class DeletePaymentMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        payment_id = kwargs["id"]
        payment = Payment.objects.get(pk=kwargs["id"])
        payment.delete()
        return DeletePaymentMutation(
            id=payment_id)