"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.models.model import Model

class Sale(Model):

    name = models.CharField(max_length=100, blank=True)
    disscount = models.FloatField(
        default=0)
    start_date = models.DateTimeField(
        blank=False, null=False, default=datetime.now)
    end_date = models.DateTimeField(
        blank=False, null=False, default=datetime.now)
    banner = models.ForeignKey(
        'models.File', related_name='sale_banners',
        blank=False, null=False, on_delete=models.PROTECT)

    user = models.ForeignKey(
        'models.User', related_name='sales',
        blank=False, null=False, on_delete=models.CASCADE)
    
    @property
    def product(self):
        return self.products.all()

    class Meta:
        db_table = '_sale'
        app_label = 'models'