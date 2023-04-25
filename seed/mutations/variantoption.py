"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Variantoption
from app.models import Variant
from seed.schema.types import Variantoption as VariantoptionType

class SaveVariantoptionMutation(graphene.Mutation):
    
    variantoption = graphene.Field(VariantoptionType)
    
    class Arguments:
        title = graphene.String(required=True)
        value = graphene.String(required=True)
        variant = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        variantoption = {}
        if "title" in kwargs:
            variantoption["title"] = kwargs["title"]
        if "value" in kwargs:
            variantoption["value"] = kwargs["value"]
        if "variant" in kwargs:
            variant = Variant.filter_permissions(
                Variant.objects,
                Variant.permission_filters(user)) \
                .get(pk=kwargs["variant"])
            variantoption["variant"] = variant
        variantoption = \
            Variantoption.objects.create(**variantoption)
        variantoption.save()
    
        return SaveVariantoptionMutation(
            variantoption=variantoption)

class SetVariantoptionMutation(graphene.Mutation):
    
    variantoption = graphene.Field(VariantoptionType)
    
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=False)
        value = graphene.String(required=False)
        variant = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        variantoption = Variantoption.filter_permissions(
            Variantoption.objects,
            Variantoption.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "title" in kwargs:
            variantoption.title = kwargs["title"]
        if "value" in kwargs:
            variantoption.value = kwargs["value"]
        if "variant" in kwargs:
            variant = Variant.objects \
                .get(pk=kwargs["variant"])
            variantoption.variant = variant
        variantoption.save()
    
        return SetVariantoptionMutation(
            variantoption=variantoption)

class DeleteVariantoptionMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        variantoption_id = kwargs["id"]
        variantoption = Variantoption.objects.get(pk=kwargs["id"])
        variantoption.delete()
        return DeleteVariantoptionMutation(
            id=variantoption_id)