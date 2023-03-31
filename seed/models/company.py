"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Company(Model):

    name = models.CharField(max_length=100, blank=True)
    common_name = models.CharField(max_length=100, blank=True)
    rfc = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(
        default=False)
    photo = models.ForeignKey(
        'models.File', related_name='company_photos',
        blank=False, null=False, on_delete=models.PROTECT)

    @property
    def users(self):
        return self.users.all()

    class Meta:
        db_table = '_company'
        app_label = 'models'