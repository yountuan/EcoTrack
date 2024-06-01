from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Sensor, Data, Alert

class SensorTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.sensor_data = {
            'type': 'AQ',
            'model': 'AQ-1000',
            'installation_date': '2024-01-01',
            'status': 'active'
        }

    def test_create_sensor(self):
        response = self.client.post('/api/sensors/', self.sensor_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Sensor.objects.count(), 1)
        self.assertEqual(Sensor.objects.get().model, 'AQ-1000')

    def test_read_sensor(self):
        sensor = Sensor.objects.create(**self.sensor_data)
        response = self.client.get(f'/api/sensors/{sensor.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['model'], 'AQ-1000')

    def test_update_sensor(self):
        sensor = Sensor.objects.create(**self.sensor_data)
        updated_data = self.sensor_data.copy()
        updated_data['model'] = 'AQ-2000'
        response = self.client.put(f'/api/sensors/{sensor.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Sensor.objects.get().model, 'AQ-2000')

    def test_delete_sensor(self):
        sensor = Sensor.objects.create(**self.sensor_data)
        response = self.client.delete(f'/api/sensors/{sensor.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Sensor.objects.count(), 0)

class DataTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.sensor = Sensor.objects.create(type='AQ', model='AQ-1000', installation_date='2024-01-01', status='active')
        self.data_payload = {
            'sensor': self.sensor.id,
            'pm25': 12.5,
            'pm10': 45.0,
            'co2': 400.0,
            'temperature': 22.5,
            'humidity': 60.0,
            'pressure': 1013.0,
            'wind_speed': 5.0,
            'wind_direction': 'N',
            'noise': 55.0,
            'light': 200.0,
            'uv_index': 3.0
        }

    def test_create_data(self):
        response = self.client.post('/api/data/', self.data_payload, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Data.objects.count(), 1)
        self.assertEqual(Data.objects.get().pm25, 12.5)

    def test_read_data(self):
        data = Data.objects.create(sensor=self.sensor, pm25=12.5, pm10=45.0, co2=400.0)
        response = self.client.get(f'/api/data/{data.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['pm25'], 12.5)

    def test_update_data(self):
        data = Data.objects.create(sensor=self.sensor, pm25=12.5, pm10=45.0, co2=400.0)
        updated_data = self.data_payload.copy()
        updated_data['pm25'] = 15.0
        response = self.client.put(f'/api/data/{data.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Data.objects.get().pm25, 15.0)

    def test_delete_data(self):
        data = Data.objects.create(sensor=self.sensor, pm25=12.5, pm10=45.0, co2=400.0)
        response = self.client.delete(f'/api/data/{data.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Data.objects.count(), 0)

class AlertTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.sensor = Sensor.objects.create(type='AQ', model='AQ-1000', installation_date='2024-01-01', status='active')
        self.alert_payload = {
            'sensor': self.sensor.id,
            'description': 'High PM2.5 levels detected',
        }

    def test_create_alert(self):
        response = self.client.post('/api/alerts/', self.alert_payload, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Alert.objects.count(), 1)
        self.assertEqual(Alert.objects.get().description, 'High PM2.5 levels detected')

    def test_read_alert(self):
        alert = Alert.objects.create(sensor=self.sensor, description='High PM2.5 levels detected')
        response = self.client.get(f'/api/alerts/{alert.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['description'], 'High PM2.5 levels detected')

    def test_update_alert(self):
        alert = Alert.objects.create(sensor=self.sensor, description='High PM2.5 levels detected')
        updated_alert = self.alert_payload.copy()
        updated_alert['description'] = 'High CO2 levels detected'
        response = self.client.put(f'/api/alerts/{alert.id}/', updated_alert, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Alert.objects.get().description, 'High CO2 levels detected')

    def test_delete_alert(self):
        alert = Alert.objects.create(sensor=self.sensor, description='High PM2.5 levels detected')
        response = self.client.delete(f'/api/alerts/{alert.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Alert.objects.count(), 0)


