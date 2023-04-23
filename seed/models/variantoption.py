"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Variantoption(Model):

    name = models.CharField(max_length=100, blank=True)
    stock = models.IntegerField(
        default=0)
    photos = models.ManyToManyField(
        'models.File', related_name='variantoption_photoses', blank=False
        )

    variant = models.ForeignKey(
        'models.Variant', related_name='variantoptions',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_variantoption'
        app_label = 'models'