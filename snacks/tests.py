# from _typeshed import Self
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# Create your tests here.

class test_Snack_page(TestCase):
  def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

  def test_about_page_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
