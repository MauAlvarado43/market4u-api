"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Opinion(Model):

    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    rate = models.IntegerField(
        default=0)

    product = models.ForeignKey(
        'models.Product', related_name='opinions',
        blank=False, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(
        'models.User', related_name='opinions',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_opinion'
        app_label = 'models'