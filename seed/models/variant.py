"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Variant(Model):

    name = models.CharField(max_length=100, blank=True)

    product = models.ForeignKey(
        'models.Product', related_name='variants',
        blank=False, null=False, on_delete=models.CASCADE)
    
    @property
    def options(self):
        return self.variantoptions.all()

    class Meta:
        db_table = '_variant'
        app_label = 'models'