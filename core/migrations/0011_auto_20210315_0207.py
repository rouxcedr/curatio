# Generated by Django 3.1.3 on 2021-03-15 02:07

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210315_0126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'verbose_name': 'Admin', 'verbose_name_plural': 'Admins'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='clientmore',
            options={'verbose_name': 'Client Data', 'verbose_name_plural': 'Clients Data'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='operator',
            options={'verbose_name': 'Operator', 'verbose_name_plural': 'Operators'},
        ),
        migrations.AlterModelOptions(
            name='operatormore',
            options={'verbose_name': 'Operator Data', 'verbose_name_plural': 'Operators Data'},
        ),
        migrations.AlterField(
            model_name='clientmore',
            name='subscription',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('EAUBELIX', 'Eau-Belix'), ('FORMATION', 'Formation')], default=None, max_length=255, null=True, verbose_name='Subscriptions'), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='clientmore',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.client'),
        ),
        migrations.AlterField(
            model_name='operatormore',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.operator'),
        ),
    ]
