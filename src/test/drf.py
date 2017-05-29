from test.mixins import RequestFactoryMixin

from rest_framework.test import APIClient as APIClientDrf
from rest_framework.test import APIRequestFactory as APIRequestFactoryDrf


class APIRequestFactory(RequestFactoryMixin, APIRequestFactoryDrf):
    pass


class APIClient(RequestFactoryMixin, APIClientDrf):
    pass
