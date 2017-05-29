#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.models import CommonModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models, transaction
from django.utils import timezone
from model_utils import Choices


class MyUserManager(BaseUserManager):

    def get_users_to_expire_in_n_days(self, days):
        pass

    def disabled_expired_users(self, send_emails=False):
        pass

    def _create_user(self, email, password, is_staff, is_superuser,
                     **extra_fields):
        pass

    def create_user(self, email, username=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)


class MyUser(AbstractBaseUser,
             CommonModel):

    # Personal Information.
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

    date_joined = models.DateTimeField(
        verbose_name='date joined',
        default=timezone.now
    )

    # Object Manager.
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
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
