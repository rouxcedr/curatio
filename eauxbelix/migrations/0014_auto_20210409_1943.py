# Generated by Django 3.1.3 on 2021-04-09 19:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eauxbelix', '0013_auto_20210409_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closednetwork',
            name='closed_network_data_shown',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('inhibitor', 'Inhibiteur'), ('cond', 'Cond'), ('ph', 'pH'), ('p', 'P'), ('m', 'M'), ('dt', 'DT'), ('iron', 'Fer'), ('copper', 'Cuivre'), ('turb', 'Turb'), ('coul', 'Coul'), ('filter', 'Filtre'), ('quantity', 'Quantité'), ('appoint', 'Appoint')], default=None, max_length=255, null=True, verbose_name='Closed Network Data Shown'), size=None),
        ),
    ]
