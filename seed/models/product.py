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
    price = models.FloatField(
        default=0)
    stock = models.IntegerField(
        default=0)
    photos = models.ManyToManyField(
        'models.File', related_name='product_photoses', blank=False
        )

    user = models.ForeignKey(
        'models.User', related_name='products',
        blank=False, null=False, on_delete=models.CASCADE)
    category = models.ForeignKey(
        'models.Category', related_name='products',
        blank=False, null=False, on_delete=models.CASCADE)
    
    @property
    def opinions(self):
        return self.opinions.all()
    @property
    def sales(self):
        return self.sales.all()
    @property
    def variants(self):
        return self.variants.all()

    class Meta:
        db_table = '_product'
        app_label = 'models'