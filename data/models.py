from django.db import models
import datetime
from django.urls import reverse

# Create your models here.


class Session(models.Model):
    CHOICES = ((0, 'Natural'), (1, 'Artificial'), (2, 'Street'))

    # General info
    name = models.CharField(max_length=64)
    training = models.TextField(max_length=500, blank=True)
    date = models.DateField(default=datetime.date.today)
    place = models.CharField(max_length=32, blank=True)
    # Environment conditions
    grass = models.IntegerField('Surface', choices=CHOICES)
    wet = models.BooleanField('Surface was wet', blank=True)
    temp = models.PositiveIntegerField('Temperature', blank=True)
    hum = models.PositiveIntegerField('Humidity', blank=True)
    additional_info = models.TextField(max_length=240, blank=True)

    def __str__(self):
        return "id:{0} name:{1}".format(str(self.pk), str(self.name))

    def get_absolute_url(self):
        return reverse('detail-session', kwargs={'pk': self.pk})

    def rained(self):
        return 'It has rained' if self.wet else "It's sunny"


class Athlete(models.Model):
    # General data
    nickname = models.CharField(max_length=16)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    data_consent = models.BooleanField()
    # Interest data
    age = models.PositiveIntegerField()
    foot_size = models.PositiveIntegerField()
    weight = models.PositiveIntegerField(help_text="Weight in Kg")
    height = models.PositiveIntegerField(help_text="Height in cm")

    def __str__(self):
        return "session:{0} name:{1}".format(str(self.session), str(self.nickname))

    def get_absolute_url(self):
        return reverse('detail-athlete', kwargs={'pk': self.pk})


class Sensor(models.Model):
    code = models.CharField(max_length=32)

    def __str__(self):
        return "code:{0}".format(str(self.code))

    def get_absolute_url(self):
        return reverse('home')


class SensorAthlete(models.Model):
    id_athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    position = models.CharField(max_length=32)

    def __str__(self):
        return "athlete: {1} sensor:{2} position:{0}".format(str(self.position), str(self.id_athlete),
                                                             str(self.id_sensor))

    def get_absolute_url(self):
        return reverse('home')


class AthleteVest(models.Model):
    id_athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    vest_num = models.IntegerField()
    time = models.CharField(max_length=8)

    def __str__(self):
        return "athlete: {1} vest:{0} time: {2}".format(str(self.vest_num), str(self.id_athlete),
                                                        str(self.time))
