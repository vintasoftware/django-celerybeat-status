from django.conf.urls import url

from celery_beat_status.views import PeriodicTasksStatusListView


urlpatterns = [
    url(r'^periodic-tasks/$', PeriodicTasksStatusListView.as_view(),
        name='periodic-tasks-status'),
]
