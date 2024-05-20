from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.translation import gettext_lazy
from django.views.generic.base import TemplateView

from celerybeat_status.helpers import get_periodic_tasks_info


class PeriodicTasksStatusListView(UserPassesTestMixin, TemplateView):
    template_name = "celerybeat_status/periodic_tasks_status_list.html"
    site_url = "/"
    login_url = "admin:login"

    def test_func(self):
        return self.request.user.is_staff and self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = gettext_lazy("Periodic tasks status")
        context["user"] = self.request.user
        context["site_url"] = self.site_url
        context["has_permission"] = self.request.user.is_superuser
        context["tasks"] = get_periodic_tasks_info()

        return context
