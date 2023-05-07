"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Product(Model):

    name = models.CharField(max_length=100, blank=True)
    short_description = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    company = models.ForeignKey(
        'models.Company', related_name='products',
        blank=False, null=False, on_delete=models.CASCADE)
    sale = models.ForeignKey(
        'models.Sale', related_name='products',
        blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(
        'models.Category', related_name='products',
        blank=False, null=False, on_delete=models.CASCADE)
    
    @property
    def opinions(self):
        return self.opinions.all()
    @property
    def variants(self):
        return self.variants.all()

    class Meta:
        db_table = '_product'
        app_label = 'models'