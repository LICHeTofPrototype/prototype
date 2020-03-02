# Generated by Django 3.0.2 on 2020-03-01 06:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analysisAPI', '0002_auto_20200201_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heartbeat',
            name='heart_beat_data',
        ),
        migrations.RemoveField(
            model_name='heartbeat',
            name='user',
        ),
        migrations.AddField(
            model_name='heartbeat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heartbeat',
            name='heart_beat_peak_time',
            field=models.FloatField(default=0, verbose_name='心拍ピーク値データ'),
        ),
        migrations.AddField(
            model_name='heartbeat',
            name='pnn_data',
            field=models.FloatField(default=0, verbose_name='PNNデータ'),
        ),
        migrations.AddField(
            model_name='heartbeat',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='heartbeat',
            name='measured_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='計測日時'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
