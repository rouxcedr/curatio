# Generated by Django 3.1.3 on 2021-04-09 14:56

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210315_0207'),
        ('eauxbelix', '0009_auto_20210315_0519'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosedNetworkMinMax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('inhibitor_min', models.FloatField()),
                ('inhibitor_max', models.FloatField()),
                ('cond_min', models.IntegerField()),
                ('cond_max', models.IntegerField()),
                ('ph_min', models.FloatField()),
                ('ph_max', models.FloatField()),
                ('p_min', models.IntegerField()),
                ('p_max', models.IntegerField()),
                ('m_min', models.IntegerField()),
                ('m_max', models.IntegerField()),
                ('dt_min', models.IntegerField()),
                ('dt_max', models.IntegerField()),
                ('iron_min', models.FloatField()),
                ('iron_max', models.FloatField()),
                ('copper_min', models.FloatField()),
                ('copper_max', models.FloatField()),
                ('turb_min', models.IntegerField()),
                ('turb_max', models.IntegerField()),
                ('coul_min', models.IntegerField()),
                ('coul_max', models.IntegerField()),
                ('filter_min', models.BooleanField()),
                ('filter_max', models.BooleanField()),
                ('quantity_min', models.FloatField()),
                ('quantity_max', models.FloatField()),
                ('appoint_min', models.FloatField()),
                ('appoint_max', models.FloatField()),
            ],
            options={
                'verbose_name': 'Closed Networks MinMax',
                'verbose_name_plural': 'Closed Network MinMax',
            },
        ),
        migrations.CreateModel(
            name='WaterTowerMinMax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Dipslide_min', models.IntegerField()),
                ('Dipslide_max', models.IntegerField()),
                ('inhibitor_min', models.IntegerField()),
                ('inhibitor_max', models.IntegerField()),
                ('cond_min', models.IntegerField()),
                ('cond_max', models.IntegerField()),
                ('orp_min', models.IntegerField()),
                ('orp_max', models.IntegerField()),
                ('cl2_libre_min', models.FloatField()),
                ('cl2_libre_max', models.FloatField()),
                ('atp_l_min', models.IntegerField()),
                ('atp_l_max', models.IntegerField()),
                ('atp_t_min', models.IntegerField()),
                ('atp_t_max', models.IntegerField()),
                ('atp_min_max', models.IntegerField()),
                ('atp_max', models.IntegerField()),
                ('iron_min', models.FloatField()),
                ('iron_max', models.FloatField()),
                ('copper_min', models.FloatField()),
                ('copper_max', models.FloatField()),
                ('p_min', models.IntegerField()),
                ('p_max', models.IntegerField()),
                ('m_min', models.IntegerField()),
                ('m_max', models.IntegerField()),
                ('cl_min', models.IntegerField()),
                ('cl_max', models.IntegerField()),
                ('appoint_min', models.FloatField()),
                ('appoint_max', models.FloatField()),
                ('purge_min', models.FloatField()),
                ('purge_max', models.FloatField()),
                ('cycle_min', models.FloatField()),
                ('cycle_max', models.FloatField()),
                ('dt_min', models.IntegerField()),
                ('dt_max', models.IntegerField()),
                ('ca_min', models.IntegerField()),
                ('ca_max', models.IntegerField()),
                ('ph_min', models.FloatField()),
                ('ph_max', models.FloatField()),
                ('bw_min', models.IntegerField()),
                ('bw_max', models.IntegerField()),
                ('p1_min', models.IntegerField()),
                ('p1_max', models.IntegerField()),
                ('p2_min', models.IntegerField()),
                ('p2_max', models.IntegerField()),
                ('p3_min', models.IntegerField()),
                ('p3_max', models.IntegerField()),
                ('p4_min', models.IntegerField()),
                ('p4_max', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Water Towers MinMax',
                'verbose_name_plural': 'Water Tower MinMax',
            },
        ),
        migrations.AlterModelOptions(
            name='closednetwork',
            options={'verbose_name': 'Closed Networks', 'verbose_name_plural': 'Closed Network'},
        ),
        migrations.AlterModelOptions(
            name='closednetworkdata',
            options={'verbose_name': 'Closed Networks Data', 'verbose_name_plural': 'Closed Network Data'},
        ),
        migrations.AlterModelOptions(
            name='watertower',
            options={'verbose_name': 'Water Towers', 'verbose_name_plural': 'Water Tower'},
        ),
        migrations.AlterModelOptions(
            name='watertowerdata',
            options={'verbose_name': 'Water Towers Data', 'verbose_name_plural': 'Water Tower Data'},
        ),
        migrations.AddField(
            model_name='boilerdata',
            name='operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.operator'),
        ),
        migrations.AddField(
            model_name='closednetwork',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='closednetwork',
            name='closed_network_data_shown',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('inhibitor', 'Inhibiteur'), ('cond', 'Cond'), ('ph', 'pH'), ('p', 'P'), ('m', 'M'), ('dt', 'DT'), ('iron', 'Iron'), ('copper', 'Cuivre'), ('turb', 'Turb'), ('coul', 'Coul'), ('filter', 'Filtre'), ('quantity', 'Pointeaux'), ('appoint', 'Appoint')], default=None, max_length=255, null=True, verbose_name='Closed Network Data Shown'), default=None, size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='closednetwork',
            name='control_chart',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='closednetwork',
            name='flow_chart',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='closednetwork',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='appoint',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='closed_network',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='closed_network_data', to='eauxbelix.closednetwork'),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='cond',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='copper',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='coul',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='dt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='filter',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='inhibitor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='iron',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='m',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.operator'),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='p',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='ph',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='closednetworkdata',
            name='turb',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertower',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watertower',
            name='control_chart',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='watertower',
            name='flow_chart',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='watertower',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watertower',
            name='water_tower_data_shown',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Dipslide', 'Dipslide'), ('inhibitor', 'Inhibiteur'), ('cond', 'Cond'), ('orp', 'ORP'), ('cl2_libre', 'CL2 Libre'), ('atp_l', 'ATP L'), ('atp_t', 'ATP T'), ('atp', 'ATP'), ('iron', 'Iron'), ('copper', 'Cuivre'), ('p', 'P'), ('m', 'M'), ('cl', 'Cl-'), ('appoint', 'Appoint'), ('purge', 'Purge'), ('cycle', 'Cycle'), ('dt', 'DT'), ('ca', 'Ca'), ('ph', 'pH'), ('bw', 'BW'), ('p1', 'P1'), ('p2', 'P2'), ('p3', 'P3'), ('p4', 'P4')], default=None, max_length=255, null=True, verbose_name='Water Tower Data Shown'), default=None, size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='Dipslide',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='appoint',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='atp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='atp_l',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='atp_t',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='bw',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='ca',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='cl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='cl2_libre',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='cond',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='copper',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='cycle',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='dt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='inhibitor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='iron',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='m',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.operator'),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='orp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='p',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='p1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='p2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='p3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='p4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='ph',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='purge',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='watertowerdata',
            name='water_tower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='water_tower_data', to='eauxbelix.boiler'),
        ),
        migrations.AddField(
            model_name='closednetwork',
            name='min_max',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eauxbelix.closednetworkminmax'),
        ),
        migrations.AddField(
            model_name='watertower',
            name='min_max',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eauxbelix.watertowerminmax'),
        ),
    ]
