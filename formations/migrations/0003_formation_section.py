# Generated by Django 3.1.3 on 2021-03-11 21:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0002_auto_20201105_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='section',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('ANALYSIS', 'Analyses'), ('PRETREATMENT', 'Prétraitement'), ('CHEMICAL_TREATMENT', 'Traitement Chimique'), ('CONTROL', 'Controle'), ('WATER_TOWER', "Tours d'eau"), ('BOILER', 'Chaudiere'), ('MICROBIOLOGY', 'Microbiologie'), ('CLOSED_NETWORK', 'Réseaux fermés')], default='ANALYSIS', max_length=255, null=True, verbose_name='Section'), null=True, size=None),
        ),
    ]
