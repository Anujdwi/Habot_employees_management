from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Employee


class EmployeeAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Obtain JWT token
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.token = response.data['access']

        # Set auth header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.employee_data = {
            'name': 'Anuj',
            'email': 'anuj@test.com',
            'department': 'Engineering',
            'role': 'Developer'
        }

    def test_create_employee(self):
        response = self.client.post('/api/employees/', self.employee_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)

    def test_create_employee_with_duplicate_email(self):
        self.client.post('/api/employees/', self.employee_data)
        response = self.client.post('/api/employees/', self.employee_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_employees(self):
        Employee.objects.create(**self.employee_data)

        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_retrieve_employee(self):
        employee = Employee.objects.create(**self.employee_data)

        response = self.client.get(f'/api/employees/{employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.employee_data['email'])

    def test_retrieve_employee_not_found(self):
        response = self.client.get('/api/employees/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_employee(self):
        employee = Employee.objects.create(**self.employee_data)

        updated_data = {
            'name': 'Updated Name',
            'email': 'anuj@test.com',
            'department': 'HR',
            'role': 'Manager'
        }

        response = self.client.put(
            f'/api/employees/{employee.id}/',
            updated_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        employee.refresh_from_db()
        self.assertEqual(employee.department, 'HR')

    def test_delete_employee(self):
        employee = Employee.objects.create(**self.employee_data)

        response = self.client.delete(f'/api/employees/{employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)

