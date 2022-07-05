from django.contrib import admin


if django_version.get_complete_version() < (4, 0, 0):
    from django.conf.urls import url, include

    urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url(r'^admin/statuscheck/', include('celerybeat_status.urls')),
    ]
else:
    from django.urls import re_path, include

    urlpatterns = [
      re_path('^admin/', admin.site.urls),
      re_path('^admin/statuscheck/', include('celerybeat_status.urls')),
    ]
