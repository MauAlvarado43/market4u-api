# Generated by Django 3.2.18 on 2023-05-04 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20230503_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.IntegerField(default=0),
        ),
    ]