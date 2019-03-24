from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as auth_views
from .views import inici
from data.admin import *

urlpatterns = [
    path('', inici, name='inici'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('data/', include('data.urls')),
    path('admin/', admin.site.urls),
    path('profile/', users_views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
]
