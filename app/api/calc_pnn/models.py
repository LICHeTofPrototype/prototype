# coding: utf-8
from django.db import models
from django.utils import timezone
# from api.account.models import User
from api.measurement.models import Measurement

# class RRIData(models.Model):
#   measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
#   RRI = models.FloatField(verbose_name="pnn_time")
#   peak_time = models.FloatField(verbose_name="pnn_time")


class BeatData(models.Model):
  beat_time = models.FloatField(verbose_name="beat_time")
  beat_data = models.FloatField(verbose_name="beat_data")

class PnnData(models.Model):
  """心拍数データ"""
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
  time = models.TimeField()
  pnn_time = models.FloatField(verbose_name="pnn_time")
  pnn = models.FloatField(verbose_name="pnn")


