from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'notes/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')

        return render(request, 'notes/profile.html', {'form': form})


class ProfileView(View):
    def get(self, request):
        return render(request, 'notes/profile.html')

    class LoginView(View):
        def get(self, request):
            form = AuthenticationForm()
            return render(request, 'notes/login.html', {'form': form})

        def post(self, request):
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('profile')  # Перенаправление на страницу профиля
            return render(request, 'notes/login.html', {'form': form})

        class ProfileView(LoginRequiredMixin, View):
            def get(self, request):
                return render(request, 'notes/profile.html')
