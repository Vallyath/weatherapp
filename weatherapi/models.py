from django.db import models

class WeatherModels(models.Model):
    date = models.CharField(max_length=255)
    temp = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)

    def __str__(self):
        return self.date + self.temp + self.desc