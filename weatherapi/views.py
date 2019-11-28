from rest_framework import viewsets

from .serializers import WeatherSerializer
from .models import WeatherModels


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = WeatherModels.objects.all()
    serializer_class = WeatherSerializer