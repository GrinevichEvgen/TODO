from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from account.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        class CustomUserChangeForm(UserChangeForm):
            class Meta:
                model = CustomUser
                fields = ('username', 'email', 'profile_picture', 'friends')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'profile_picture', 'friends')
