from rest_framework import serializers

from .models import WeatherModels

class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeatherModels
        fields = ('date', 'temp', 'desc')