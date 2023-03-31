"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Opinion
from app.models import Product
from app.models import User
from seed.schema.types import Opinion as OpinionType

class SaveOpinionMutation(graphene.Mutation):
    
    opinion = graphene.Field(OpinionType)
    
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        rate = graphene.Int(required=True)
        product = graphene.Int(required=True)
        user = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        opinion = {}
        if "title" in kwargs:
            opinion["title"] = kwargs["title"]
        if "description" in kwargs:
            opinion["description"] = kwargs["description"]
        if "rate" in kwargs:
            opinion["rate"] = kwargs["rate"]
        if "product" in kwargs:
            product = Product.filter_permissions(
                Product.objects,
                Product.permission_filters(user)) \
                .get(pk=kwargs["product"])
            opinion["product"] = product
        if "user" in kwargs:
            user = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["user"])
            opinion["user"] = user
        opinion = \
            Opinion.objects.create(**opinion)
        opinion.save()
    
        return SaveOpinionMutation(
            opinion=opinion)

class SetOpinionMutation(graphene.Mutation):
    
    opinion = graphene.Field(OpinionType)
    
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=False)
        description = graphene.String(required=False)
        rate = graphene.Int(required=False)
        product = graphene.Int(required=False)
        user = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        opinion = Opinion.filter_permissions(
            Opinion.objects,
            Opinion.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "title" in kwargs:
            opinion.title = kwargs["title"]
        if "description" in kwargs:
            opinion.description = kwargs["description"]
        if "rate" in kwargs:
            opinion.rate = kwargs["rate"]
        if "product" in kwargs:
            product = Product.objects \
                .get(pk=kwargs["product"])
            opinion.product = product
        if "user" in kwargs:
            user = User.objects \
                .get(pk=kwargs["user"])
            opinion.user = user
        opinion.save()
    
        return SetOpinionMutation(
            opinion=opinion)

class DeleteOpinionMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        opinion_id = kwargs["id"]
        opinion = Opinion.objects.get(pk=kwargs["id"])
        opinion.delete()
        return DeleteOpinionMutation(
            id=opinion_id)