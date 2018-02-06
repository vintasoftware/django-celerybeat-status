
from celerybeat_status.tests.utils import (
    SuperuserBaseTestCase, TestRequiresSuperuser)

try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse


class PeriodicTaskStatusListTests(
        TestRequiresSuperuser, SuperuserBaseTestCase):
    view_name = 'periodic-tasks-status'

    def setUp(self):
        super().setUp()
        self.view_url = reverse(self.view_name)
