# Generated by Django 3.2.18 on 2023-05-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0007_auto_20230430_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(choices=[('NS', 'NS'), ('AGUASCALIENTES', 'AGUASCALIENTES'), ('BAJA_CALIFORNIA', 'BAJA_CALIFORNIA'), ('BAJA_CALIFORNIA_SUR', 'BAJA_CALIFORNIA_SUR'), ('CAMPECHE', 'CAMPECHE'), ('COAHUILA', 'COAHUILA'), ('COLIMA', 'COLIMA'), ('CHIAPAS', 'CHIAPAS'), ('CHIHUAHUA', 'CHIHUAHUA'), ('DURANGO', 'DURANGO'), ('CIUDAD_DE_MEXICO', 'CIUDAD_DE_MEXICO'), ('GUANAJUATO', 'GUANAJUATO'), ('GUERRERO', 'GUERRERO'), ('HIDALGO', 'HIDALGO'), ('JALISCO', 'JALISCO'), ('MEXICO', 'MEXICO'), ('MICHOACAN', 'MICHOACAN'), ('MORELOS', 'MORELOS'), ('NAYARIT', 'NAYARIT'), ('NUEVO_LEON', 'NUEVO_LEON'), ('OAXACA', 'OAXACA'), ('PUEBLA', 'PUEBLA'), ('QUERETARO', 'QUERETARO'), ('QUINTANA_ROO', 'QUINTANA_ROO'), ('SAN_LUIS_POTOSI', 'SAN_LUIS_POTOSI'), ('SINALOA', 'SINALOA'), ('SONORA', 'SONORA'), ('TABASCO', 'TABASCO'), ('TAMAULIPAS', 'TAMAULIPAS'), ('TLAXCALA', 'TLAXCALA'), ('VERACRUZ', 'VERACRUZ'), ('YUCATAN', 'YUCATAN'), ('ZACATECAS', 'ZACATECAS')], max_length=64),
        ),
    ]
