from django.conf.urls import url

from celerybeat_status.views import PeriodicTasksStatusListView


urlpatterns = [
    url(r'^periodic-tasks/$', PeriodicTasksStatusListView.as_view(),
        name='periodic-tasks-status'),
]
