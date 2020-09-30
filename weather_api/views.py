from django.shortcuts import render
from rest_framework import generics

from .permissions import IsAuthorOrReadOnly
from .models import Weather
from .serializer import WeatherSerializer
from rest_framework import permissions
# Create your views here.

class WeatherList(generics.ListCreateAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

class WeatherDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
