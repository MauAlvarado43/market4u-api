# Generated by Django 3.2.18 on 2023-04-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]