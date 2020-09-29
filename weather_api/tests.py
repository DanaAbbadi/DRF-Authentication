from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Weather
# Create your tests here.

class WeatherTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test_user', password='password')
        test_user.save()

        test_post = Weather.objects.create(
            user = test_user,
            region = 'MENA region',
            country = 'Jordan',
            status = 'Sunny',
            date = 'September 30, 2020',

        )
        test_post.save() # Save the object to mock Database

    def test_weather_content(self):
        weather = Weather.objects.get(id=1)
        actual_user = str(weather.user)
        actual_region = str(weather.region)
        actual_country = str(weather.country)
        actual_status = str(weather.status)
        actual_date = str(weather.date)

        self.assertEqual(actual_user, 'test_user')
        self.assertEqual(actual_region, 'MENA region')
        self.assertEqual(actual_country, 'Jordan')
        self.assertEqual(actual_status, 'Sunny')
        self.assertEqual(actual_date, 'September 30, 2020')

    def test_api_permissions(self):
        response = self.client.get(reverse('weather'))
        # User doesn't have access token
        self.assertEqual(response.status_code, 401)