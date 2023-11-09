from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Repeat password",widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
