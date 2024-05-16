from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # The new admin catch-all view will break URL patterns routed after the admin URLs and matching
    # the admin URL prefix. Source: https://docs.djangoproject.com/en/5.0/releases/3.2/#id1
    path(
        "admin/statuscheck/",
        include("celerybeat_status.urls", namespace="celerybeat_status"),
    ),
    path("admin/", admin.site.urls),
]
