from django.utils import version as django_version

from celerybeat_status.tests.utils import (
    SuperuserBaseTestCase, TestRequiresSuperuser)

if django_version.get_complete_version() < (2, 0, 0):
    from django.core.urlresolvers import reverse
else:
    from django.urls import reverse


class PeriodicTaskStatusListTests(
        TestRequiresSuperuser, SuperuserBaseTestCase):
    view_name = 'periodic-tasks-status'

    def setUp(self):
        super(PeriodicTaskStatusListTests, self).setUp()
        self.view_url = reverse(self.view_name)
