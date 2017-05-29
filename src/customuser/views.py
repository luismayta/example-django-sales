#!/usr/bin/env python
# -*- coding: utf-8 -*-

from customuser.models import MyUser
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken as ObtainToken
from rest_framework.response import Response

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


class ObtainAuthToken(ObtainToken):
    """Overrides the default ObtainAuthToken for token auth."""

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_active': user.is_active,
            },
        })
