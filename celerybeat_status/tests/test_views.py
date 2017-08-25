from django.core.urlresolvers import reverse

from core.tests.utils import (
    SuperuserBaseTestCase, TestRequiresSuperuser)


class PeriodicTaskStatusListTests(
        TestRequiresSuperuser, SuperuserBaseTestCase):
    view_name = 'periodic-tasks-status'

    def setUp(self):
        super().setUp()
        self.view_url = reverse(self.view_name)
