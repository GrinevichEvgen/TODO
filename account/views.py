from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.shortcuts import render, redirect
from django.views import View

from .forms import CustomUserChangeForm


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Перенаправление на страницу профиля
        return render(request, 'account/register.html', {'form': form})


class CustomLoginView(DjangoLoginView):
    template_name = 'account/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('profile')  # Перенаправление на страницу профиля


class ProfileView(View):
    def get(self, request):
        return render(request, 'account/profile.html')


class HomeView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'account/register.html', {'form': form})


class LogoutView(DjangoLogoutView):
    pass


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'account/profile.html', {'form': form})
