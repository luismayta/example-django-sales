import os

import dj_database_url
from sales.settings import *

TEST_RUNNER = 'django_behave.runner.DjangoBehaveTestSuiteRunner'
DEBUG = True

db = dj_database_url.parse(os.getenv('DB_TEST_URL'))
db['ENGINE'] = 'tenant_schemas.postgresql_backend'

DATABASES = {
    'default': db,
}

INSTALLED_APPS += (
    'behave_django',
)
