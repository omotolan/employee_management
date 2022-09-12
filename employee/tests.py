from django.test import TestCase
from django.urls import reverse

from employee import models


# Create your tests here.

class view_test(TestCase):

    def test_to_create(self):
        # employee = models.Employee()
        # employee.first_name = "tolani"
        # employee.last_name = "akinsola"
        # response = self.client.request(employee)
        # self.assertEqual(response.st)
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)

