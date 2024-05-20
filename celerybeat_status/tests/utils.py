from django.contrib.auth import get_user_model
from django.test import Client, TestCase

User = get_user_model()


class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.regular_user = User.objects.create_user(
            username="regular",
            email="regular@email.com",
            password="123",
            is_staff=False,
            is_superuser=False,
        )
        self.staff_user = User.objects.create_user(
            username="staff",
            email="staff@email.com",
            password="123",
            is_staff=True,
            is_superuser=False,
        )
        self.superuser = User.objects.create_user(
            username="super",
            email="superuser@gmail.com",
            password="123",
            is_staff=True,
            is_superuser=True,
        )


class TestRequiresAuthenticatedUser(object):

    def test_requires_authenticated_user(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 302)
