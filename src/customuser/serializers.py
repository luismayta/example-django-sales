#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Rest customuser Serializer.'''
from customuser.models import MyUser
from rest_framework import serializers


class MyUserSerializer(serializers.ModelSerializer):

    def current_user(self):
        return self.context.get('request').user

    class Meta:

        model = MyUser

        read_only_fields = (
            'is_active',
            'created',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }
