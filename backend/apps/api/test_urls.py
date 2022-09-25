from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from apps.projects.models import Project

User = get_user_model()


class URLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.auth_user = User.objects.create_user(
            username='tester',
            email='test@test.com',
        )

    def setUp(self):
        self.auth_client = Client()
        self.guest_client = Client()
        self.auth_client.force_login(self.auth_user)

    def test_api_guest_access(self):
        response = self.guest_client.get('http://127.0.0.1:8000/api/projects/')
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_api_auth_access(self):
        response = self.auth_client.get('http://127.0.0.1:8000/api/projects/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
