from django.urls import path, include
from .views import WeatherList, WeatherDetails

urlpatterns = [
    path('', WeatherList.as_view(), name='weather'), 
    path('<int:pk>/', WeatherDetails.as_view(), name='weather_details')  
]