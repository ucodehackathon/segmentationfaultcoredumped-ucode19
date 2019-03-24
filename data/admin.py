from django.contrib import admin
from .models import Session
from .models import Athlete
from .models import Sensor
from .models import SensorAthlete
from .models import AthleteVest

# Register your models here.
admin.site.register(Session)
admin.site.register(Athlete)
admin.site.register(Sensor)
admin.site.register(SensorAthlete)
admin.site.register(AthleteVest)
