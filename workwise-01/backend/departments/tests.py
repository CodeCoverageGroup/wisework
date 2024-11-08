# pylint: disable=no-member
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from departments.models import Department  # Adjust path based on the structure


class DepartmentAPITestCase(APITestCase):
    """
    Test cases for CRUD operations on Department model with JWT-based authentication.
    """

    def setUp(self):
        """
        Set up a test user, obtain JWT access token, and define the department list URL.
        Also set authorization headers for authenticated requests.
        """
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create JWT token for the test user
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # Define department API URL
        self.department_list_url = reverse('department-list')  # Using DRF's router naming

        # Set headers for authenticated requests
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_create_department(self):
        """
        Test creating a new department.

        Expects:
            - HTTP 201 Created status code.
            - Department count to increase by 1.
            - Created department name matches the provided name.
        """
        data = {
            'name': 'HR Department',
            'description': 'Handles human resources'
        }
        response = self.client.post(self.department_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), 1)
        self.assertEqual(Department.objects.get().name, 'HR Department')

    def test_get_department_list(self):
        """
        Test retrieving the list of departments.

        Expects:
            - HTTP 200 OK status code.
            - Response data contains all created departments.
        """
        # Create sample departments
        Department.objects.create(name='HR Department', description='Handles HR')
        Department.objects.create(name='Finance Department', description='Handles Finance')

        response = self.client.get(self.department_list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Ensure two departments are returned

    def test_update_department(self):
        """
        Test updating an existing department's details.

        Expects:
            - HTTP 200 OK status code.
            - Department's name and description are updated as expected.
        """
        # Create a department to update
        department = Department.objects.create(name='Marketing', description='Handles marketing')

        update_url = reverse('department-detail', kwargs={'pk': department.pk})
        data = {'name': 'Updated Marketing', 'description': 'Updated description'}

        response = self.client.put(update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the update
        department.refresh_from_db()
        self.assertEqual(department.name, 'Updated Marketing')
        self.assertEqual(department.description, 'Updated description')

    def test_delete_department(self):
        """
        Test deleting an existing department.

        Expects:
            - HTTP 204 No Content status code.
            - Department count decreases by 1, indicating successful deletion.
        """
        # Create a department to delete
        department = Department.objects.create(name='IT Department', description='Handles IT')

        delete_url = reverse('department-detail', kwargs={'pk': department.pk})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify deletion
        self.assertEqual(Department.objects.count(), 0)
        