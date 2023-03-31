"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.models.model import Model

class Sale(Model):

    disscount = models.FloatField(
        default=0)
    start_date = models.DateTimeField(
        blank=False, null=False, default=datetime.now)
    end_date = models.DateTimeField(
        blank=False, null=False, default=datetime.now)

    product = models.ForeignKey(
        'models.Product', related_name='sales',
        blank=False, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
        'models.User', related_name='sales',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_sale'
        app_label = 'models'