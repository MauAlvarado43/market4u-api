"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Message
from app.models import User
from seed.schema.types import Message as MessageType

class SaveMessageMutation(graphene.Mutation):
    
    message = graphene.Field(MessageType)
    
    class Arguments:
        content = graphene.String(required=True)
        sender = graphene.Int(required=True)
        target = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        message = {}
        if "content" in kwargs:
            message["content"] = kwargs["content"]
        if "sender" in kwargs:
            sender = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["sender"])
            message["sender"] = sender
        if "target" in kwargs:
            target = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["target"])
            message["target"] = target
        message = \
            Message.objects.create(**message)
        message.save()
    
        return SaveMessageMutation(
            message=message)

class SetMessageMutation(graphene.Mutation):
    
    message = graphene.Field(MessageType)
    
    class Arguments:
        id = graphene.Int(required=True)
        content = graphene.String(required=False)
        sender = graphene.Int(required=False)
        target = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        message = Message.filter_permissions(
            Message.objects,
            Message.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "content" in kwargs:
            message.content = kwargs["content"]
        if "sender" in kwargs:
            sender = User.objects \
                .get(pk=kwargs["sender"])
            message.sender = sender
        if "target" in kwargs:
            target = User.objects \
                .get(pk=kwargs["target"])
            message.target = target
        message.save()
    
        return SetMessageMutation(
            message=message)

class DeleteMessageMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        message_id = kwargs["id"]
        message = Message.objects.get(pk=kwargs["id"])
        message.delete()
        return DeleteMessageMutation(
            id=message_id)