# Generated by Django 3.1.3 on 2021-03-15 02:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eauxbelix', '0007_auto_20210313_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoilerControlChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Boiler Control Chart',
                'verbose_name_plural': 'Boilers Control Chart',
            },
        ),
        migrations.AlterModelOptions(
            name='boiler',
            options={'verbose_name': 'Boiler', 'verbose_name_plural': 'Boilers'},
        ),
        migrations.AlterModelOptions(
            name='boilerdata',
            options={'verbose_name': 'Boiler Data', 'verbose_name_plural': 'Boilers Data'},
        ),
        migrations.AlterModelOptions(
            name='boilerminmax',
            options={'verbose_name': 'Boiler MinMax', 'verbose_name_plural': 'Boilers MinMax'},
        ),
        migrations.AddField(
            model_name='boiler',
            name='boiler_data_shown',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('inhihitor', 'Inhibiteur'), ('p', 'P'), ('m', 'M'), ('oh', 'OH'), ('cl', 'Cl-'), ('so3', 'SO3'), ('cond', 'Cond'), ('pointeaux', 'Pointeaux'), ('mbd', 'MBD(s)'), ('on_off', 'On / Off'), ('vapor_pound_kg', 'Vapeur(lbs / kg)'), ('vaper_cond', 'Vapeur(Cond)')], default=None, max_length=255, null=True, verbose_name='Boiler Data Shown'), default=[('m', 'M')], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boilerminmax',
            name='name',
            field=models.CharField(default='BoilerMinMax1', max_length=100),
            preserve_default=False,
        ),
    ]
