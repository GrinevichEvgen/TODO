import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class AddNoteForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(max_length=1000, widget=forms.Textarea)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    nickname = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(required=True, min_value=1, max_value=120)
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+?1?\d{9,15}$', phone):
            raise ValidationError('Введите правильный номер телефона.')
        return phone

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise ValidationError('Возраст должен быть не менее 18 лет.')
        return age