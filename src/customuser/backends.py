#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Model Backends. """
from customuser.models import MyUser
from django.contrib.auth.models import BaseUserManager


class EmailBackend(object):

    """Class Email BackEnd. """

    def authenticate(self, **kwargs):  # pylint: disable=no-self-use
        """Authenticate function."""
        email = kwargs.get('username')
        password = kwargs.get('password')
        try:
            if email:
                user = MyUser.objects.get(  # pylint: disable=no-member
                    email=BaseUserManager.normalize_email(email.lower())
                )
                if user.check_password(password):
                    return user
        except MyUser.DoesNotExist:  # pylint: disable=no-member
            return None

    def get_user(self, user_id):  # pylint: disable=no-self-use
        """get user function."""
        try:
            return MyUser.objects.get(id=user_id)  # pylint: disable=no-member
        except MyUser.DoesNotExist:  # pylint: disable=no-member
            return None
