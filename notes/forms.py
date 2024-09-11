from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddNoteForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(max_length=1000, widget=forms.Textarea)


class RegisterForm(UserCreationForm):
    model = User
    fields = ['username', 'email', 'password1', 'password2']
