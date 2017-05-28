#!/usr/bin/env python
# -*- coding: utf-8 -*-

from customuser.models import MyUser
from rest_framework import viewsets

from .serializers import MyUserSerializer


class MyUserViewSet(viewsets.ModelViewSet):
    """ Class MyUserViewSet. """

    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    filter_fields = (
        'email',
        'is_active',
        'created',
    )
    ordering = (
        'created',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
    )

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(self.request.data.get('password'))
        user.save()

    def perform_update(self, serializer):
        user = serializer.save()
        password = self.request.data.get('password')
        if password:
            user.set_password(password)
            user.save()
