"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Category
from seed.schema.types import Category as CategoryType

class SaveCategoryMutation(graphene.Mutation):
    
    category = graphene.Field(CategoryType)
    
    class Arguments:
        name = graphene.String(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        category = {}
        if "name" in kwargs:
            category["name"] = kwargs["name"]
        category = \
            Category.objects.create(**category)
        category.save()
    
        return SaveCategoryMutation(
            category=category)

class SetCategoryMutation(graphene.Mutation):
    
    category = graphene.Field(CategoryType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        category = Category.filter_permissions(
            Category.objects,
            Category.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "name" in kwargs:
            category.name = kwargs["name"]
        category.save()
    
        return SetCategoryMutation(
            category=category)

class DeleteCategoryMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        category_id = kwargs["id"]
        category = Category.objects.get(pk=kwargs["id"])
        category.delete()
        return DeleteCategoryMutation(
            id=category_id)