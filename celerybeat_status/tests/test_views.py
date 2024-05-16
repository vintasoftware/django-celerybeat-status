from django.utils import version as django_version
from django.urls import reverse

from celerybeat_status.tests.utils import SuperuserBaseTestCase, TestRequiresSuperuser


class PeriodicTaskStatusListTests(TestRequiresSuperuser, SuperuserBaseTestCase):
    view_name = "celerybeat_status:periodic-tasks-status"

    def setUp(self):
        super(PeriodicTaskStatusListTests, self).setUp()
        self.view_url = reverse(self.view_name)
