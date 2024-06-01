from django.contrib import admin
from .models import Data, Alert, Sensor

admin.site.register(Data)
admin.site.register(Alert)
admin.site.register(Sensor)