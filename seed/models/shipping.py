"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Shipping(Model):
    
    STATUSES = (
        ('CREATED', 'CREATED'),
        ('SENT', 'SENT'),
        ('COMPLETED', 'COMPLETED'),
        ('CANCELED', 'CANCELED'),
    )

    info = models.TextField(blank=True)
    folio = models.CharField(max_length=200, blank=True)
    address = models.TextField(blank=True)
    status = models.CharField(
        max_length=64, choices=STATUSES,
        blank=False)
    total = models.FloatField(
        default=0)
    subtotal = models.FloatField(
        default=0)
    shipment = models.FloatField(
        default=0)

    cart = models.ForeignKey(
        'models.Cart', related_name='shippings',
        blank=False, null=False, on_delete=models.CASCADE)
    buyer = models.ForeignKey(
        'models.User', related_name='buyer_shippings',
        blank=True, null=True, on_delete=models.CASCADE)
    company = models.ForeignKey(
        'models.Company', related_name='shippings',
        blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = '_shipping'
        app_label = 'models'