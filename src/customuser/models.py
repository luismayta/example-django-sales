#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.models import CommonModel
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models, transaction
from django.utils import timezone
from model_utils import Choices


class MyUserManager(BaseUserManager):

    def get_users_to_expire_in_n_days(self, days):
        pass

    def disabled_expired_users(self, send_emails=False):
        pass

    def create_user(self, email, username, first_name, last_name, password,
                    *args, **kwargs):
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name.title(),
            last_name=last_name.title(),
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name,
                         password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            first_name=first_name.title(),
            last_name=last_name.title(),
        )
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user


class MyUserQuerySet(models.QuerySet):
    pass


class MyUser(AbstractBaseUser, PermissionsMixin, CommonModel):

    username = models.CharField(
        max_length=100,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=100,
        unique=True,
        help_text='Email Personal.'
    )

    first_name = models.CharField(
        max_length=150,
        help_text='Personal Info.'
    )

    last_name = models.CharField(
        max_length=150,
        help_text='Personal Info.'
    )

    # Status.
    STATUS = Choices(
        'ACTIVATED',
        'DEACTIVATED',
        'BANNED',
        'PENDING',
        'REJECTED',
    )

    status = models.CharField(
        choices=STATUS,
        default='PENDING',
        max_length=15,
        blank=True,
        null=True,
        help_text='User status',
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

    date_joined = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='date joined',
        default=timezone.now,
    )

    # Object Manager.
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name',
    ]

    def __str__(self):
        return self.email

    @transaction.atomic
    def save(self, *args, **kwargs):
        super(MyUser, self).save(*args, **kwargs)

    class Meta:
        db_table = 'myuser'
        ordering = ['-created']
