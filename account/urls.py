from django.contrib.auth import views as auth_views
from django.urls import path

from .views import RegisterView, ProfileView

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),  # URL для входа
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

]
