# Generated by Django 2.2.10 on 2020-03-28 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('measurement', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PnnData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnn_data', models.FloatField(verbose_name='pnn')),
                ('measurement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='measurement.Measurement')),
            ],
        ),
        migrations.CreateModel(
            name='BeatData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beat_data', models.TextField(max_length=6105, verbose_name='beat_data')),
                ('measurement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='measurement.Measurement')),
            ],
        ),
    ]
