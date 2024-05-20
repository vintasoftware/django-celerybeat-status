# Django Celery Beat Status

![PyPI - Version](https://img.shields.io/pypi/v/django-celerybeat-status)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/django-celerybeat-status.svg)
![Supported Django Versions](https://img.shields.io/pypi/frameworkversions/django/django-celerybeat-status.svg)
[![Build Status](https://github.com/vintasoftware/django-celerybeat-status/actions/workflows/tests.yml/badge.svg)](https://github.com/vintasoftware/django-celerybeat-status/actions/workflows/tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/vintasoftware/django-celerybeat-status/badge.svg?branch=main)](https://coveralls.io/github/vintasoftware/django-celerybeat-status?branch=main)

A library that integrates with django admin and shows in a simple GUI when your periodic are going to run next.

## Instalation

```bash
pip install django-celerybeat-status
```

## Configuration

1. Add `"celerybeat_status"` to your `INSTALLED_APPS` variable in django settings

```python
INSTALLED_APPS = [
  ...
  "celerybeat_status",
]
```

2. Create a url for the status check view

```python
from django.urls import include, path

urlpatterns = [
  # other urls...
  path("admin/statuscheck/", include("celerybeat_status.urls")),  # celerybeat_status admin
  path("admin/", admin.site.urls),  # django admin
]
```

## Usage

Check your tasks under `/admin/statuscheck/periodic-tasks/` (if you configured your urls the way we suggested in this docs).

You can also find a link in `/admin` sidebar.

How you admin page will look like:

![admin-page](https://raw.githubusercontent.com/vintasoftware/django-celerybeat-status/master/README_IMAGES/django-celerybeat-status-admin.png)

How your tasks will be shown:

![tasks-page](https://raw.githubusercontent.com/vintasoftware/django-celerybeat-status/master/README_IMAGES/django-celerybeat-status-tasks.png)

## Contributing

### Setting up the development environment

1. Clone the repository.

2. Create a virtual environment.

3. Install the dependencies.

```bash
pip install -r requirements_test.txt
```

4. Run the project. Relevant to check UI changes.

```bash
# Create the database and run the migrations.
python manage.py migrate
# Create a superuser. This will allow you to access the admin interface.
python manage.py createsuperuser
# Start the development server. You can view the application by navigating to the URL provided in the terminal.
python manage.py runserver
```

5. Run the tests. This package uses `tox` to run tests on multiple evironments, please make sure they are passing before submitting a pull request.

```bash
tox
```

## Commercial Support

This project, as other Vinta open-source projects, is used in products of Vinta clients. We are always looking for exciting work, so if you need any commercial support, feel free to get in touch: contact@vinta.com.br

Copyright (c) 2017 Vinta Serviços e Soluções Tecnológicas Ltda
