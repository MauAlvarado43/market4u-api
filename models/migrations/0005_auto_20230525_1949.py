# Generated by Django 3.2.18 on 2023-05-26 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_alter_user_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='cp',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
