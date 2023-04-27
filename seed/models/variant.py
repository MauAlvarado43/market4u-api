"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Variant(Model):

    price = models.FloatField(
        default=0)
    stock = models.IntegerField(
        default=0)
    photos = models.ManyToManyField(
        'models.File', related_name='variant_photoses', blank=False
        )
    shipment = models.FloatField(
        default=0)

    product = models.ForeignKey(
        'models.Product', related_name='variants',
        blank=False, null=False, on_delete=models.CASCADE)
    
    @property
    def options(self):
        return self.variantoptions.all()

    class Meta:
        db_table = '_variant'
        app_label = 'models'