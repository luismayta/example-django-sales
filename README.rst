sales
#############################

|build_status| |code_climate| |github_tag| |issues_count| |github_issues| |test_coverage| |license|

:Version: 0.0.0
:Web: https://bitbucket.org/devdiana/sales
:Download: http://bitbucket.org/devdiana/sales
:Source: http://bitbucket.org/devdiana/sales
:Keywords: sales

Sales system Retail

.. contents:: Table of Contents:
    :local:

Requirements
============

This is a list of applications that need to be installed previously to enjoy all the goodies of this configuration:

- `Python 3.6.1`_
- `Docker`_

Flight To Infinity... and Beyond
--------------------------------

First, we need to install some requiments inside a virtualenv and then we have to build and run up all the services. Then we need to migrate our database and create a super user in order to acced the admin (http://localhost/admin/).

.. code-block:: bash

  $ pip install -r requirements/dev.txt
  $ docker-compose up --build
  $ docker-compose run --rm web make migrate
  $ docker-compose run --rm web make pm action=createsuperuser
  $ docker-compose run --rm web make pm action=populate  # Populate with default data

- Do not forget to stop your postgresql service if this is running on the 5432 port.

Then, we run a local development server doing this.

.. code-block:: bash

  $ docker-compose run --rm --service-ports web make runserver

In order to run the shell of Django we need to run this.

.. code-block:: bash

  $ docker-compose run --rm web make pm action=shell

Or another command, without any argument.

.. code-block:: bash

  $ docker-compose run --rm web make pm action={another command}

In order to delete your database and create another one we need to enter the
container doing something like this:

.. code-block:: bash

  $ docker ps  # We need to identify the container_id.
  $ docker exec -it {posgis_container_id} bash
  $ dropdb $POSTGRES_DB -U $POSTGRES_USER
  $ createdb $POSTGRES_DB -U $POSTGRES_USER


Developing
==========

Sales depends a django - Python web framework.


Environment
-----------

.. code-block:: bash

  export AWS_ACCESS_KEY_ID=xxxxxxxxxxxxxxxxxxxx
  export AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  export AWS_DEFAULT_REGION=us-west-2
  export FLASK_DEBUG=1


Environment variables on your AWS Console
-----------------------------------------

Set environment variables on your AWS console.

.. code-block:: bash

  export POSITIVA_COD_SERVICIO=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  export POSITIVA_APP_CONSUMIDORA=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  export POSITIVA_USER=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  export POSITIVA_PASSWORD=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

  export FACEBOOK_APP_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  export FACEBOOK_APP_VERSION=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  export FACEBOOK_APP_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  export FACEBOOK_PAGE_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  export FACEBOOK_VERIFY_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


Others
------

Other commands for developing are written in Makefile:

.. code-block:: bash

λ make help
  Commands:
    build                Build docker container
    clean                clean Files compiled
    runserver            Runserver
    up                   Up application
    deploy               Deploy Application
    environment          Make environment for developer
    documentation        Make Documentation
    install              Install Dependences
    lint                 Clean files unnecesary
    test                 make test
    help                 Show help text


Changelog
=========

Please see `changelog`_ for more information what has changed recently.

Contributing
============

Please see `contributing`_ for details.

Credits
=======

Made with :heart: :coffee:️and :pizza: by `company`_.

- `All Contributors`_

.. |code_climate| image:: https://codeclimate.com/github/devdiana/sales/badges/gpa.svg
  :target: https://codeclimate.com/github/devdiana/sales
  :alt: Code Climate

.. |github_tag| image:: https://img.shields.io/github/tag/devdiana/sales.svg?maxAge=2592000
  :target: https://bitbucket.org/devdiana/sales
  :alt: Github Tag

.. |build_status| image:: https://travis-ci.org/devdiana/sales.svg
  :target: https://travis-ci.org/devdiana/sales
  :alt: Build Status Tag

.. |github_issues| image:: https://img.shields.io/github/issues/devdiana/sales.svg
  :target: https://bitbucket.org/devdiana/saleshadenlabs/cookiecutter-python-project/issues
  :alt: Github Issues

.. |issues_count| image:: https://codeclimate.com/github/devdiana/sales/badges/issue_count.svg
  :target: https://codeclimate.com/github/devdiana/sales
  :alt: Issue Count

.. |license| image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square
  :target: LICENSE
  :alt: License

.. |test_coverage| image:: https://codeclimate.com/github/devdiana/sales/badges/coverage.svg
  :target: https://codeclimate.com/github/devdiana/sales/coverage
  :alt: Test Coverage

..
   Links

.. _`changelog`: CHANGELOG.rst
.. _`contributors`: AUTHORS
.. _`contributing`: CONTRIBUTING.rst
.. _`company`: https://bitbucket.org/devdiana
.. _`author`: https://github.com/luismayta
