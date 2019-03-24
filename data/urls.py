from django.urls import path
from django.contrib import admin
from .views import SessionsView
from .views import SessionView
from .views import SessionEditView
from .views import SessionDeleteView
from .views import SensorDeleteView
from .views import SensorEditView
from .views import SessionCreateView
from .views import AthleteCreateView
from .views import AthleteEditView
from .views import AthleteDeleteView
from .views import SensorCreateView
from .views import AthleteView
from .views import SensorAssignView

urlpatterns = [
    path('', SessionsView.as_view(), name='home'),
    path('sessions/new/', SessionCreateView.as_view(), name='new-session'),
    path('sessions/<int:pk>/', SessionView.as_view(), name='detail-session'),
    path('sessions/<int:pk>/edit/', SessionEditView.as_view(), name='edit-session'),
    path('sessions/<int:pk>/del/', SessionDeleteView.as_view(), name='del-session'),
    path('athletes/new/', AthleteCreateView.as_view(), name='new-athlete'),
    path('athletes/<int:pk>/', AthleteView.as_view(), name='detail-athlete'),
    path('athletes/<int:pk>/edit/', AthleteEditView.as_view(), name='edit-athlete'),
    path('athletes/<int:pk>/del/', AthleteDeleteView.as_view(), name='del-athlete'),
    path('sensors/new/', SensorCreateView.as_view(), name='new-sensor'),
    path('sensors/<int:pk>/del/', SensorDeleteView.as_view(), name='del-sensor'),
    path('sensors/<int:pk>/edit/', SensorEditView.as_view(), name='edit-sensor'),
    path('sensors/sensor/assign/', SensorAssignView.as_view(), name='assign-sensor')
]