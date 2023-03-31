"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Purchase(Model):

    amount = models.IntegerField(
        default=0)
    product = models.JSONField(
        blank=True, default=dict)
    sale = models.JSONField(
        blank=True, default=dict)

    cart = models.ForeignKey(
        'models.Cart', related_name='purchases',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_purchase'
        app_label = 'models'