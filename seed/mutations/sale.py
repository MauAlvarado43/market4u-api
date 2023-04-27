"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Sale
from app.models import User
from app.models import File
from seed.schema.types import Sale as SaleType

class SaveSaleMutation(graphene.Mutation):
    
    sale = graphene.Field(SaleType)
    
    class Arguments:
        name = graphene.String(required=True)
        disscount = graphene.Float(required=True)
        startDate = graphene.DateTime(required=True)
        endDate = graphene.DateTime(required=True)
        banner = graphene.Int(required=True)
        user = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        sale = {}
        if "name" in kwargs:
            sale["name"] = kwargs["name"]
        if "disscount" in kwargs:
            sale["disscount"] = kwargs["disscount"]
        if "startDate" in kwargs:
            sale["start_date"] = kwargs["startDate"]
        if "endDate" in kwargs:
            sale["end_date"] = kwargs["endDate"]
        if "user" in kwargs:
            user = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["user"])
            sale["user"] = user
        if "banner" in kwargs:
            banner = File.filter_permissions(
                File.objects,
                File.permission_filters(user)) \
                .get(pk=kwargs["banner"])
            sale["banner"] = banner
        sale = \
            Sale.objects.create(**sale)
        sale.save()
    
        return SaveSaleMutation(
            sale=sale)

class SetSaleMutation(graphene.Mutation):
    
    sale = graphene.Field(SaleType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        disscount = graphene.Float(required=False)
        startDate = graphene.DateTime(required=False)
        endDate = graphene.DateTime(required=False)
        banner = graphene.Int(required=False)
        user = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        sale = Sale.filter_permissions(
            Sale.objects,
            Sale.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "name" in kwargs:
            sale.name = kwargs["name"]
        if "disscount" in kwargs:
            sale.disscount = kwargs["disscount"]
        if "startDate" in kwargs:
            sale.start_date = kwargs["startDate"]
        if "endDate" in kwargs:
            sale.end_date = kwargs["endDate"]
        if "user" in kwargs:
            user = User.objects \
                .get(pk=kwargs["user"])
            sale.user = user
        if "banner" in kwargs:
            banner = File.objects \
                .get(pk=kwargs["banner"])
            sale.banner = banner
        sale.save()
    
        return SetSaleMutation(
            sale=sale)

class DeleteSaleMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        sale_id = kwargs["id"]
        sale = Sale.objects.get(pk=kwargs["id"])
        sale.delete()
        return DeleteSaleMutation(
            id=sale_id)