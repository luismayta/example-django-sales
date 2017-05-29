import django
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import CommandError
from django.db import connection


class TestCaseMixin(object):

    @classmethod
    def assert_test_database(cls):
        """
        Raises a CommandError in the event that the database name does not contain
        any reference to testing.

        Also checks South settings to ensure migrations are not implemented.
        """

        if 'test' not in settings.DATABASES['default']['NAME']:
            raise CommandError('You must run with a test database')

    @classmethod
    def setUpClass(cls):
        cls.assert_test_database()
        cursor = connection.cursor()
        cursor.execute('DROP SCHEMA IF EXISTS public CASCADE')
        cursor.execute('CREATE SCHEMA IF NOT EXISTS public')
        cls.sync()

    @classmethod
    def tearDownClass(cls):
        cursor = connection.cursor()
        cursor.execute('DROP SCHEMA IF EXISTS public CASCADE')
        call_command('flush', interactive=False, load_initial_data=False)

    @classmethod
    def sync(cls):
        if django.VERSION >= (1, 7, 0):
            call_command('migrate',
                         interactive=False,
                         verbosity=0)
        else:
            call_command('syncdb',
                         public=True,
                         interactive=False,
                         migrate_all=True,
                         verbosity=0)
