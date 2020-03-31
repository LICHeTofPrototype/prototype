# Generated by Django 2.2.10 on 2020-03-31 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calc_data', '0003_pnndata_pnn_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beatdata',
            name='beat_data',
            field=models.TextField(verbose_name='beat_data'),
        ),
        migrations.AlterField(
            model_name='beatdata',
            name='measurement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='measurement.Measurement'),
        ),
        migrations.AlterField(
            model_name='pnndata',
            name='measurement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='measurement.Measurement'),
        ),
        migrations.AlterField(
            model_name='pnndata',
            name='pnn_data',
            field=models.TextField(verbose_name='pnn'),
        ),
        migrations.AlterField(
            model_name='pnndata',
            name='pnn_time',
            field=models.TextField(verbose_name='pnn_time'),
        ),
    ]