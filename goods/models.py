from django.db import models

class Sensor(models.Model):
    SENSOR_TYPES = (
        ('AQ', 'Air Quality'),
        ('TM', 'Temperature'),
        ('PR', 'Pressure'),
        ('WS', 'Wind Speed'),
        ('WD', 'Wind Direction'),
        ('NO', 'Noise'),
        ('LT', 'Light'),
        ('UV', 'UV Index'),
    )
    
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, choices=SENSOR_TYPES)
    model = models.CharField(max_length=50)
    installation_date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.model} ({self.type})"

class Data(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='data', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    co2 = models.FloatField()

    def __str__(self):
        return f"Data from {self.sensor} at {self.timestamp}"

class Alert(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='alerts', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"Alert for {self.sensor} at {self.timestamp}"
