from django.test import TestCase
from django.test.client import Client


class TestIfRootRendersHTML(TestCase):
    def test_animals_can_speak(self):
        c = Client()
        resp = c.get('/')
        self.assertEquals(resp.status_code, 200)
