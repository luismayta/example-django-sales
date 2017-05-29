from test.drf import APIClient
from test.mixins import TestCaseMixin


class TestCase(TestCaseMixin):
    client_class = APIClient
