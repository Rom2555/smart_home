from datetime import datetime

from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=False)

    def __str__(self): return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    image = models.ImageField(upload_to='measurements/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.temperature) + ' ' + 'C'

