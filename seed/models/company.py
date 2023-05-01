"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Company(Model):
    
    STATES = (
        ('NS', 'NS'),
        ('AGUASCALIENTES', 'AGUASCALIENTES'),
        ('BAJA CALIFORNIA', 'BAJA CALIFORNIA'),
        ('BAJA CALIFORNIA SUR', 'BAJA CALIFORNIA SUR'),
        ('CAMPECHE', 'CAMPECHE'),
        ('COAHUILA', 'COAHUILA'),
        ('COLIMA', 'COLIMA'),
        ('CHIAPAS', 'Chiapas'),
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

    name = models.CharField(max_length=100, blank=True)
    common_name = models.CharField(max_length=100, blank=True)
    rfc = models.CharField(max_length=20, blank=True)
    cp = models.IntegerField(
        default=0)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(
        default=False)
    photo = models.ForeignKey(
        'models.File', related_name='company_photos',
        blank=False, null=False, on_delete=models.PROTECT)
    municipality = models.CharField(max_length=100, blank=True)
    state = models.CharField(
        max_length=64, choices=STATES,
        blank=False)
    cologn = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)

    @property
    def users(self):
        return self.users.all()

    class Meta:
        db_table = '_company'
        app_label = 'models'