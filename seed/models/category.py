"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Category(Model):

    name = models.CharField(max_length=100, blank=True)

    @property
    def products(self):
        return self.products.all()

    class Meta:
        db_table = '_category'
        app_label = 'models'