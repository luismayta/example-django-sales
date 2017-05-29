#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import MyUser


class CleanNamesForm(forms.ModelForm):

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name.title()

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return last_name.title()


class UserSignupForm(CleanNamesForm):

    """
    Form User Creation.
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        max_length=255,
        min_length=6,
    )
    password1 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
    )

    def clean_password1(self):
        # Checks that the two password entries match.
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password != password1:
            raise forms.ValidationError('Passwords don\'t match')
        return password1

    def save(self, commit=True):
        # Save the provided password in hashed format.
        user = super(UserSignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = MyUser
        fields = '__all__'


class UserChangeForm(CleanNamesForm):

    """ Form User Change Form.

    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField(
        help_text='Raw passwords are not stored, so there is no way to see '
        'this user\'s password, but you can change the password '
        'using <a href=\'../password/\'>this form</a>.'
    )

    class Meta:
        model = MyUser
        fields = '__all__'

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value.
        return self.initial['password']


class UserLoginForm(forms.Form):

    """A form to login users by username or email."""

    username = forms.CharField(
        max_length=100,
    )  # Could be an email or username.
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput,
    )

    user = None  # Will be used to continue the redirect in LoginView.

    error_messages = {
        'incorrect_login': (
            'Lo sentimos, ha ingresado un usuario o contraseña incorrecta.'
        ),
        'inactive_account': 'Lo sentimos, esta cuenta se encuentra inactiva :(',
    }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserLoginForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError(
                self.error_messages['incorrect_login']
            )
        username = username.lower()
        if MyUser.objects.filter(username=username).exists() or \
                MyUser.objects.filter(email=username).exists():
            return username
        raise forms.ValidationError(
            self.error_messages['incorrect_login']
        )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not username:
            raise forms.ValidationError(
                self.error_messages['incorrect_login']
            )
        user = authenticate(
            username=username,
            password=password,
        )
        if not user:
            raise forms.ValidationError(
                self.error_messages['incorrect_login']
            )
        elif not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive_account']
            )
        self.user = user
