"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Payment(Model):
    
    TYPES = (
        ('DEBIT', 'DEBIT'),
        ('CREDIT', 'CREDIT'),
    )

    card_number = models.CharField(max_length=100, blank=True)
    expire_date = models.CharField(max_length=10, blank=True)
    type = models.CharField(
        max_length=64, choices=TYPES,
        blank=False)
    address = models.CharField(max_length=200, blank=True)
    bank = models.CharField(max_length=100, blank=True)

    user = models.ForeignKey(
        'models.User', related_name='payments',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_payment'
        app_label = 'models'