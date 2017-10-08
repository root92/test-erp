***********************
Introduction & Settings
***********************

Introduction
============

ERP Platform for managing Universities in Guinea.
It's Based on Docker, Django and Postgres

Setup
=====

No local setup should be needed apart from:
- `docker <https://docs.docker.com/engine/installation/>`__
- `docker-compose <https://docs.docker.com/compose/>`__

The local dev setup uses **docker-compose** to spin up all necessary services.
Make sure you have it installed and can connect to the **docker daemon**.

Build the app
-------------

Run in project directory after you clone the repository:

.. code:: bash

    docker-compose build

Run the app
===========

Start the dev server
------------------

Run in project directory:

.. code:: bash

    docker-compose up

This will build and download the containers and start them. The ``docker-compose.yml``
file describes the setup of the containers.

The web server should be reachable at ``http://localhost:8080``.

Create a user
-------------

To login to the app or the django admin, a superuser needs to be created with:

.. code:: bash

    docker-compose run gn-erp manage createsuperuser


Run commands on the server
==========================

Each docker container uses the same script as entrypoint. The ``entrypoint.sh``
script offers a range of commands to start services or run commands.
The full list of commands can be seen in the script.
The pattern to run a command is always
``docker-compose run <container-name> <entrypoint-command> <...args>``

The following are some examples:

+-------------------------------------+----------------------------------------------------------+
| Action                              | Command                                                  |
+=====================================+==========================================================+
| Generate documentation              | ``docker-compose gn-erp gen_docs``                       |
+-------------------------------------+----------------------------------------------------------+
| Run tests                           | ``docker-compose run gn-erp test``                       |
+-------------------------------------+----------------------------------------------------------+
| Create a shell inside the container | ``docker-compose run gn-erp bash``                       |
+-------------------------------------+----------------------------------------------------------+
| Run django manage.py                | ``docker-compose run gn-erp manage help``                |
+-------------------------------------+----------------------------------------------------------+
| Create a python shell               | ``docker-compose run gn-erp manage shell``               |
+-------------------------------------+----------------------------------------------------------+
| Create a postgresql shell           | ``docker-compose run gn-erp manage dbshell``             |
+-------------------------------------+----------------------------------------------------------+
| Create pending ORM migration files  | ``docker-compose run gn-erp manage makemigrations``      |
+-------------------------------------+----------------------------------------------------------+
| Apply pending ORM migrations        | ``docker-compose run gn-erp manage migrate``             |
+-------------------------------------+----------------------------------------------------------+
| Show ORM migrations                 | ``docker-compose run gn-erp manage showmigrations``      |
+-------------------------------------+----------------------------------------------------------+


Containers and services
=======================

These are the list of the main containers we will have at the end of the project:

+-----------+-------------------------------------------------------------------------+
| Container | Description                                                             |
+===========+=========================================================================+
| gn-erp    | `Django <https://www.djangoproject.com/>`__                         |
+-----------+-------------------------------------------------------------------------+
| db        | `PostgreSQL <https://www.postgresql.org/>`__ database                   |
+-----------+-------------------------------------------------------------------------+
| couchdb   | `CouchDB <http://couchdb.apache.org/>`__ database for sync              |
+-----------+-------------------------------------------------------------------------+
| rq        | `RQ python <http://python-rq.org/>`__ task runner to perform jobs       |
+-----------+-------------------------------------------------------------------------+
| redis     | `Redis <https://redis.io/>`__ for task queueing and task result storage |
+-----------+-------------------------------------------------------------------------+

All of the container definitions for development can be found in the ``docker-compose.yml``.

.. note:: Postgresql uses Django ORM models for table configuration and migrations.
