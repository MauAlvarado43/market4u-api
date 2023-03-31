"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Cart(Model):

    destiny = models.CharField(max_length=200, blank=True)

    user = models.ForeignKey(
        'models.User', related_name='carts',
        blank=False, null=False, on_delete=models.CASCADE)
    payment = models.ForeignKey(
        'models.Payment', related_name='carts',
        blank=False, null=False, on_delete=models.CASCADE)
    
    @property
    def purchases(self):
        return self.purchases.all()

    class Meta:
        db_table = '_cart'
        app_label = 'models'