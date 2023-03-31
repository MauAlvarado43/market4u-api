"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Message(Model):

    content = models.TextField(blank=True)

    sender = models.ForeignKey(
        'models.User', related_name='sender_messages',
        blank=False, null=False, on_delete=models.CASCADE)
    target = models.ForeignKey(
        'models.User', related_name='target_messages',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_message'
        app_label = 'models'