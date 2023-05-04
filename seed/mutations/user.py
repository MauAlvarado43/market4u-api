"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import User
from app.models import Company
from app.models import File
from seed.schema.types import User as UserType

class SaveUserMutation(graphene.Mutation):
    
    user = graphene.Field(UserType)
    
    class Arguments:
        username = graphene.String(required=True)
        firstName = graphene.String(required=True)
        lastName = graphene.String(required=True)
        email = graphene.String(required=True)
        isActive = graphene.Boolean(required=True)
        password = graphene.String(required=True)
        active = graphene.Boolean(required=True)
        photo = graphene.Int(required=False)
        type = graphene.String(required=True)
        token = graphene.String(required=True)
        tokenVerified = graphene.Boolean(required=True)
        code = graphene.Int(required=False)
        street = graphene.String(required=True)
        city = graphene.String(required=True)
        cp = graphene.Int(required=True)
        municipality = graphene.String(required=True)
        state = graphene.String(required=True)
        cologn = graphene.String(required=True)
        telephone = graphene.String(required=True)
        company = graphene.Int(required=False)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        user = {}
        if "userName" in kwargs:
            user["user_name"] = kwargs["userName"]
        if "firstName" in kwargs:
            user["first_name"] = kwargs["firstName"]
        if "lastName" in kwargs:
            user["last_name"] = kwargs["lastName"]
        if "email" in kwargs:
            user["email"] = kwargs["email"]
        if "isActive" in kwargs:
            user["is_active"] = kwargs["isActive"]
        if "active" in kwargs:
            user["active"] = kwargs["active"]
        if "type" in kwargs:
            user["type"] = kwargs["type"]
        if "token" in kwargs:
            user["token"] = kwargs["token"]
        if "tokenVerified" in kwargs:
            user["token_verified"] = kwargs["tokenVerified"]
        if "code" in kwargs:
            user["code"] = kwargs["code"]
        if "street" in kwargs:
            user["street"] = kwargs["street"]
        if "city" in kwargs:
            user["city"] = kwargs["city"]
        if "cp" in kwargs:
            user["cp"] = kwargs["cp"]
        if "municipality" in kwargs:
            user["municipality"] = kwargs["municipality"]
        if "state" in kwargs:
            user["state"] = kwargs["state"]
        if "cologn" in kwargs:
            user["cologn"] = kwargs["cologn"]
        if "telephone" in kwargs:
            user["telephone"] = kwargs["telephone"]
        if "photo" in kwargs:
            photo = File.filter_permissions(
                File.objects,
                File.permission_filters(user)) \
                .get(pk=kwargs["photo"])
            user["photo"] = photo
        if "company" in kwargs:
            company = Company.filter_permissions(
                Company.objects,
                Company.permission_filters(user)) \
                .get(pk=kwargs["company"])
            user["company"] = company
        user = \
            User.objects.create(**user)
        if "password" in kwargs: user.set_password(kwargs["password"])
        user.save()
    
        return SaveUserMutation(
            user=user)

class SetUserMutation(graphene.Mutation):
    
    user = graphene.Field(UserType)
    
    class Arguments:
        id = graphene.Int(required=True)
        username = graphene.String(required=False)
        firstName = graphene.String(required=False)
        lastName = graphene.String(required=False)
        email = graphene.String(required=False)
        isActive = graphene.Boolean(required=False)
        password = graphene.String(required=False)
        active = graphene.Boolean(required=False)
        photo = graphene.Int(required=False)
        token = graphene.String(required=False)
        tokenVerified = graphene.Boolean(required=False)
        code = graphene.Int(required=False)
        type = graphene.String(required=False)
        street = graphene.String(required=False)
        city = graphene.String(required=False)
        cp = graphene.Int(required=False)
        municipality = graphene.String(required=False)
        state = graphene.String(required=False)
        cologn = graphene.String(required=False)
        telephone = graphene.String(required=False)
        company = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        user = User.filter_permissions(
            User.objects,
            User.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "userName" in kwargs:
            user.user_name = kwargs["userName"]
        if "firstName" in kwargs:
            user.first_name = kwargs["firstName"]
        if "lastName" in kwargs:
            user.last_name = kwargs["lastName"]
        if "email" in kwargs:
            user.email = kwargs["email"]
        if "isActive" in kwargs:
            user.is_active = kwargs["isActive"]
        if "password" in kwargs:
            user.set_password(kwargs["password"])
        if "active" in kwargs:
            user.active = kwargs["active"]
        if "type" in kwargs:
            user.type = kwargs["type"]
        if "token" in kwargs:
            user.token = kwargs["token"]
        if "tokenVerified" in kwargs:
            user.token_verified = kwargs["tokenVerified"]
        if "code" in kwargs:
            user.code = kwargs["code"]
        if "street" in kwargs:
            user.street = kwargs["street"]
        if "city" in kwargs:
            user.city = kwargs["city"]
        if "cp" in kwargs:
            user.cp = kwargs["cp"]
        if "municipality" in kwargs:
            user.municipality = kwargs["municipality"]
        if "state" in kwargs:
            user.state = kwargs["state"]
        if "cologn" in kwargs:
            user.cologn = kwargs["cologn"]
        if "telephone" in kwargs:
            user.telephone = kwargs["telephone"]
        if "photo" in kwargs:
            photo = File.objects \
                .get(pk=kwargs["photo"])
            user.photo = photo
        if "company" in kwargs:
            company = Company.objects \
                .get(pk=kwargs["company"])
            user.company = company
        user.save()
    
        return SetUserMutation(
            user=user)

class DeleteUserMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        user_id = kwargs["id"]
        user = User.objects.get(pk=kwargs["id"])
        user.delete()
        return DeleteUserMutation(
            id=user_id)