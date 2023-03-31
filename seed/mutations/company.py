"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Company
from app.models import File
from seed.schema.types import Company as CompanyType

class SaveCompanyMutation(graphene.Mutation):
    
    company = graphene.Field(CompanyType)
    
    class Arguments:
        name = graphene.String(required=True)
        commonName = graphene.String(required=True)
        rfc = graphene.String(required=True)
        address = graphene.String(required=True)
        phone = graphene.String(required=True)
        email = graphene.String(required=True)
        active = graphene.Boolean(required=True)
        photo = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        company = {}
        if "name" in kwargs:
            company["name"] = kwargs["name"]
        if "commonName" in kwargs:
            company["common_name"] = kwargs["commonName"]
        if "rfc" in kwargs:
            company["rfc"] = kwargs["rfc"]
        if "address" in kwargs:
            company["address"] = kwargs["address"]
        if "phone" in kwargs:
            company["phone"] = kwargs["phone"]
        if "email" in kwargs:
            company["email"] = kwargs["email"]
        if "active" in kwargs:
            company["active"] = kwargs["active"]
        if "photo" in kwargs:
            photo = File.filter_permissions(
                File.objects,
                File.permission_filters(user)) \
                .get(pk=kwargs["photo"])
            company["photo"] = photo
        company = \
            Company.objects.create(**company)
        company.save()
    
        return SaveCompanyMutation(
            company=company)

class SetCompanyMutation(graphene.Mutation):
    
    company = graphene.Field(CompanyType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        commonName = graphene.String(required=False)
        rfc = graphene.String(required=False)
        address = graphene.String(required=False)
        phone = graphene.String(required=False)
        email = graphene.String(required=False)
        active = graphene.Boolean(required=False)
        photo = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        company = Company.filter_permissions(
            Company.objects,
            Company.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "name" in kwargs:
            company.name = kwargs["name"]
        if "commonName" in kwargs:
            company.common_name = kwargs["commonName"]
        if "rfc" in kwargs:
            company.rfc = kwargs["rfc"]
        if "address" in kwargs:
            company.address = kwargs["address"]
        if "phone" in kwargs:
            company.phone = kwargs["phone"]
        if "email" in kwargs:
            company.email = kwargs["email"]
        if "active" in kwargs:
            company.active = kwargs["active"]
        if "photo" in kwargs:
            photo = File.objects \
                .get(pk=kwargs["photo"])
            company.photo = photo
        company.save()
    
        return SetCompanyMutation(
            company=company)

class DeleteCompanyMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        company_id = kwargs["id"]
        company = Company.objects.get(pk=kwargs["id"])
        company.delete()
        return DeleteCompanyMutation(
            id=company_id)