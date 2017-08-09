# Django Celery Beat Status

A library that integrates with django admin and shows in a simple GUI when your periodic are going to run next.

## Instalation

``` bash
pip install git+https://github.com/hugobessa/django_model_tenants.git#master
```

## Configuration

1. Add `'celery_beat_status'` to your `INSTALLED_APPS` variable in django settings

``` python
INSTALLED_APPS = [
  ...
  'celery_beat_status',
]
```

2. Create a url for the status check view

```python
from django.conf.urls import url, include

urlpatterns = [
  # other urls...
  url(r'^admin/statuscheck/', include('celery_beat_status.urls', namespace="celery_beat_status")),`
]
```

## Usage

Just access django admin and you'll know what to do.


## Commercial Support

This project, as other Vinta open-source projects, is used in products of Vinta clients. We are always looking for exciting work, so if you need any commercial support, feel free to get in touch: contact@vinta.com.br

Copyright (c) 2017 Vinta Serviços e Soluções Tecnológicas Ltda