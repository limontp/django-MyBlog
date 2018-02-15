from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput)
    password_conf = forms.CharField(label='Repeat password', max_length=32, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class LoginForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)