from django.test import TestCase
from django.urls import reverse


class HealthCheckTests(TestCase):
    def test_feed_loads(self):
        response = self.client.get(reverse("thought-list"))
        self.assertEqual(response.status_code, 200)

