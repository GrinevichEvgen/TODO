from django.urls import path
from .views import register, home

urlpatterns = [
    path('', register, name='register'),
    path('home/', home, name='home'),
]
