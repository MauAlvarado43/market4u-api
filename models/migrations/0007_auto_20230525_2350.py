# Generated by Django 3.2.18 on 2023-05-26 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_auto_20230525_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shippings', to='models.company'),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]