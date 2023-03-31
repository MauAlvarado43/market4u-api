"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from seed.models.model import Model

class User(AbstractUser, Model):
    
    TYPES = (
        ('SUPERADMIN', 'SUPERADMIN'),
        ('ADMIN;SELLER', 'ADMIN;SELLER'),
        ('NORMAL', 'NORMAL'),
    )

    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    active = models.BooleanField(
        default=False)
    type = models.CharField(
        max_length=64, choices=TYPES,
        blank=False)
    photo = models.ForeignKey(
        'models.File', related_name='user_photos',
        blank=False, null=False, on_delete=models.PROTECT)

    company = models.ForeignKey(
        'models.Company', related_name='users',
        blank=True, null=True, on_delete=models.CASCADE)
    
    @property
    def carts(self):
        return self.carts.all()
    @property
    def products(self):
        return self.products.all()
    @property
    def whishlist(self):
        return self.products.all()
    @property
    def sales(self):
        return self.sales.all()

    class Meta:
        db_table = '_user'
        app_label = 'models'