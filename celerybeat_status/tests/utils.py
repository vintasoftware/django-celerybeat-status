from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseTestCase(TestCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.user_email = 'user@email.com'
        self.user_password = 'the_password'
        self.user = User.objects.create_user(
            username='testuser', email=self.user_email, 
            password=self.user_password)

        self.auth_client = Client()
        self.auth_client.force_login(self.user)


class SuperuserBaseTestCase(BaseTestCase):

    def setUp(self):
        self.superuser_email = 'superuser@email.com'
        self.superuser_password = 'the_password'
        self.superuser = User.objects.create_superuser(
            username='testsuperuser',
            email=self.superuser_email,
            password=self.superuser_password)

        self.super_client = Client()
        self.super_client.force_login(self.superuser)

        super(SuperuserBaseTestCase, self).setUp()


class TestRequiresAuthenticatedUser(object):

    def test_requires_authenticated_user(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 302)


class TestRequiresSuperuser(TestRequiresAuthenticatedUser):

    def test_requires_superuser(self):
        response = self.auth_client.get(self.view_url)
        self.assertEqual(response.status_code, 302)

    def test_superuser_get_request_success(self):
        response = self.super_client.get(self.view_url)
        self.assertEqual(response.status_code, 200)