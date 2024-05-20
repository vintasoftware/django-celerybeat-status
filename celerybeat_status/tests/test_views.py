from django.contrib.auth import get_user_model
from django.urls import reverse

from celerybeat_status.tests.utils import BaseTestCase, TestRequiresAuthenticatedUser

User = get_user_model()


class PeriodicTasksStatusListViewTests(TestRequiresAuthenticatedUser, BaseTestCase):
    view_name = "celerybeat_status:periodic-tasks-status"

    def setUp(self):
        super().setUp()
        self.view_url = reverse(self.view_name)

    def test_non_authenticated_user_is_redirected(self):
        response = self.client.get(self.view_url)
        self.assertRedirects(response, "/admin/login/?next=" + self.view_url)

    def test_regular_user_access_returns_forbidden(self):
        self.client.force_login(self.regular_user)
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 403)

    def test_staff_user_access_returns_forbidden(self):
        self.client.force_login(self.staff_user)
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 403)

    def test_superuser_access_returns_success(self):
        self.client.force_login(self.superuser)
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)
