#!/usr/bin/env python
# -*- coding: utf-8 -*-
from customuser.models import MyUser
from factory import Sequence
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):

    class Meta:
        model = MyUser
        django_get_or_create = (
            'email',
            'password',
        )
    email = Sequence(lambda n: 'email #%s' % n)
    password = 'P@ssw0rd'
    first_name = 'hacker'
    last_name = 'cracker'
    mobile = '051959196850'
