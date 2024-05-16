from django.urls import path

from celerybeat_status.views import PeriodicTasksStatusListView

app_name = "celerybeat_status"

urlpatterns = [
    path(
        "periodic-tasks/",
        PeriodicTasksStatusListView.as_view(),
        name="periodic-tasks-status",
    ),
]
