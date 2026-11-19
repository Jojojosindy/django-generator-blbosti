from django.test import SimpleTestCase
from django.urls import reverse


class GeneratorTests(SimpleTestCase):
    def test_home_returns_html_and_a_quote(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Generátor zbytečných moudrostí")
        self.assertIn("hlaska", response.context)

    def test_health_returns_ok(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "ok"})

    def test_previous_does_not_repeat(self):
        response = self.client.get(reverse("home") + "?previous=0")
        self.assertNotEqual(response.context["selected"], 0)
