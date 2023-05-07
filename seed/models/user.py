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
        ('ADMIN', 'ADMIN'),
        ('SELLER', 'SELLER'),
        ('NORMAL', 'NORMAL'),
    )
    STATES = (
        ('NS', 'NS'),
        ('AGUASCALIENTES', 'AGUASCALIENTES'),
        ('BAJA CALIFORNIA', 'BAJA CALIFORNIA'),
        ('BAJA CALIFORNIA SUR', 'BAJA CALIFORNIA SUR'),
        ('CAMPECHE', 'CAMPECHE'),
        ('COAHUILA', 'COAHUILA'),
        ('COLIMA', 'COLIMA'),
        ('CHIAPAS', 'CHIAPAS'),
        ('CHIHUAHUA', 'CHIHUAHUA'),
        ('DURANGO', 'DURANGO'),
        ('CIUDAD DE MEXICO', 'CIUDAD DE MEXICO'),
        ('GUANAJUATO', 'GUANAJUATO'),
        ('GUERRERO', 'GUERRERO'),
        ('HIDALGO', 'HIDALGO'),
        ('JALISCO', 'JALISCO'),
        ('MEXICO', 'MEXICO'),
        ('MICHOACAN', 'MICHOACAN'),
        ('MORELOS', 'MORELOS'),
        ('NAYARIT', 'NAYARIT'),
        ('NUEVO LEON', 'NUEVO LEON'),
        ('OAXACA', 'OAXACA'),
        ('PUEBLA', 'PUEBLA'),
        ('QUERETARO', 'QUERETARO'),
        ('QUINTANA ROO', 'QUINTANA ROO'),
        ('SAN LUIS POTOSI', 'SAN LUIS POTOSI'),
        ('SINALOA', 'SINALOA'),
        ('SONORA', 'SONORA'),
        ('TABASCO', 'TABASCO'),
        ('TAMAULIPAS', 'TAMAULIPAS'),
        ('TLAXCALA', 'TLAXCALA'),
        ('VERACRUZ', 'VERACRUZ'),
        ('YUCATAN', 'YUCATAN'),
        ('ZACATECAS', 'ZACATECAS'),
    )

    active = models.BooleanField(
        default=False)
    photo = models.ForeignKey(
        'models.File', related_name='user_photos',
        blank=True, null=True, on_delete=models.PROTECT)
    type = models.CharField(
        max_length=64, choices=TYPES,
        blank=False)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    cp = models.IntegerField(
        default=0)
    municipality = models.CharField(max_length=100, blank=True)
    state = models.CharField(
        max_length=64, choices=STATES,
        blank=False)
    cologn = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=100, blank=True)
    token = models.CharField(max_length=40, blank=True)
    token_verified = models.BooleanField(
        default=False)
    code = models.IntegerField(
        default=0)

    company = models.ForeignKey(
        'models.Company', related_name='users',
        blank=True, null=True, on_delete=models.CASCADE)
    wishlist = models.ManyToManyField(
        'models.Product', related_name='wishlist_users', blank=True,
        db_table='_user__wishlist')
    
    @property
    def carts(self):
        return self.buyer_carts.all()
    @property
    def shippings(self):
        return self.seller_shippings.all()

    class Meta:
        db_table = '_user'
        app_label = 'models'