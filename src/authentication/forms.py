from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm as AuthForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from .models import RegisterUser


class AuthenticationForm(AuthForm):
    """Formulario de login."""

    def __init__(self, *args, **kwargs):
        auth_type = settings.AUTHENTICATION_TYPE.lower()
        super().__init__(*args, **kwargs)
        if auth_type == 'email':
            self.fields['username'].label = 'Tu email'
        if auth_type == 'both':
            self.fields['username'].label = 'Nombre de usuario o email'


class RegisterUserForm(forms.ModelForm):
    """Formulario de registro."""

    password2 = forms.CharField(
        label='Repetir contraseña',
        widget=forms.PasswordInput()
    )

    class Meta:
        model = RegisterUser
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        return make_password(password)

    def clean_password2(self):
        password = self.data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError(
                'Las contraseñas deben ser iguales'
            )
        return password2

    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username):
            raise forms.ValidationError(
                'Nombre de usuario ya existe'
            )
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email):
            raise forms.ValidationError(
                'Email ya existe'
            )
        return email
