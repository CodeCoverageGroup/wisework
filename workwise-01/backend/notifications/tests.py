# pylint: disable=no-member
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Notification
from rest_framework_simplejwt.tokens import RefreshToken

class NotificationTests(APITestCase):
    """
    Test suite for the Notification API, focusing on creating and retrieving notifications.
    """

    def setUp(self):
        """
        Set up the test environment by creating a test user, obtaining a JWT token, 
        and configuring the Authorization header for API requests.
        """
        # Create user
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Obtain JWT token for the user
        self.client = APIClient()
        self.token = RefreshToken.for_user(self.user).access_token

        # Set Authorization header with JWT token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # URLs
        self.notification_url = reverse('notification-list')

    def test_create_notification(self):
        """
        Test the creation of a notification.

        Verifies:
            - HTTP 201 Created status code.
            - The Notification object is successfully created in the database.
        """
        data = {
            'user': self.user.id,
            'title': 'Test Notification',
            'message': 'This is a test notification'
        }
        response = self.client.post(self.notification_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Notification.objects.count(), 1)

    def test_get_notifications(self):
        """
        Test retrieving a list of notifications for the authenticated user.

        Verifies:
            - HTTP 200 OK status code.
            - The response contains the expected number of notifications.
        """
        Notification.objects.create(user=self.user, title='Test Notification', message='This is a test notification')
        response = self.client.get(self.notification_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
