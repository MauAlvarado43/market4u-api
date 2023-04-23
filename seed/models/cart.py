"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Cart(Model):

    buyer = models.ForeignKey(
        'models.User', related_name='buyer_carts',
        blank=False, null=False, on_delete=models.CASCADE)
    payment = models.ForeignKey(
        'models.Payment', related_name='carts',
        blank=False, null=False, on_delete=models.CASCADE)
    
    @property
    def shippings(self):
        return self.shippings.all()

    class Meta:
        db_table = '_cart'
        app_label = 'models'