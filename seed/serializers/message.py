"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Message
from app.models import User

class MessageSerializer(serializers.ModelSerializer):

    sender_id = serializers.PrimaryKeyRelatedField(
        source='sender', queryset=User.objects.all(),
        required=True, allow_null=False)
    target_id = serializers.PrimaryKeyRelatedField(
        source='target', queryset=User.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Message
        fields = (
            'id',
            'created_at',
            'hash',
            'content',
            'sender_id',
            'target_id',  
        )