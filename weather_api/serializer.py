from rest_framework import serializers

from .models import Weather

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','user','region', 'country', 'status', 'date')
        model = Weather