================================================
 KRONOS Intranet - Django Application Container
================================================

About
-----
For Django_ applications that are hostet on the **KRONOS Intranet**
this project container provides adequat templates and base configuration.

An application should base its templates on "base.html" and add an entry into
the urls.py file of this project.

Installation
------------
To avoid conflicts, this project should be installed into a virtualenv. Just
clone the repository and the contained sub-repos with the following command:

``clone https://lmoppert@bitbucket.org/LEV_AppDev/app-container she``

There are some prerequisites you have to provide before you can install the
necessary python packages:

* MySQL server must be installed including mysql_config. For Debian/Ubuntu, you
  should install 

  ``mysql-common, mysql-server, libmysqlclient-dev``
* In order to build some packages, the python development files should be
  isntalled, Debian/Ubuntu:

  ``python-dev``

The actual installation is the done with 

``pip install -r requirements.txt``

Currently the requirement definition of the ``django-filer`` package is broken
so the dependencies are explicitly mentioned in the ``requirements.txt`` file
and you can install it manually after the above installation has finished:
``pip install django-filer --no-deps``


.. _Django: https://www.djangoproject.com/