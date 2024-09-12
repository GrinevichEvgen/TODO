from django.contrib.auth.views import LoginView
from django.urls import path
from .views import RegisterView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('login/', LoginView.as_view(), name='login'),  # URL для входа
]
