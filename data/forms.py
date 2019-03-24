from django import forms
from betterforms.multiform import MultiModelForm

from .models import Session
from .models import Athlete
from .models import AthleteVest
from .models import Sensor
from .models import SensorAthlete


class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = ('name', 'training', 'date', 'place', 'grass', 'wet', 'temp', 'hum', 'additional_info')


class AthleteForm(forms.ModelForm):

    class Meta:
        model = Athlete
        fields = ('nickname', 'age', 'foot_size', 'weight', 'height', 'data_consent')


class AthleteVestForm(forms.ModelForm):

    class Meta:
        model = AthleteVest
        fields = ('id_sensor', 'vest_num')


class SensorForm(forms.ModelForm):

    class Meta:
        model = Sensor
        fields = 'code'


class SensorAthleteForm(forms.ModelForm):

    class Meta:
        model = SensorAthlete
        fields = 'position'


class AthleteMultiForm(MultiModelForm):
    form_classes = {
        'athlete': AthleteForm,
        'sensor_athlete': SensorAthleteForm,
        'athlete_vest': AthleteVestForm,
    }


