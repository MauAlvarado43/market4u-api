# Generated by Django 3.2.18 on 2023-04-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_sale_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='shipment',
            field=models.FloatField(default=0),
        ),
    ]