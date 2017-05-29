from test.mixins import TestCaseMixin
from rest_framework.test import APIClient


class TestCase(TestCaseMixin):
    client_class = APIClient
