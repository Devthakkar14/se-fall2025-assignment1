from django.test import TestCase
from django.urls import reverse


class PollsViewTests(TestCase):
    """Basic tests for the polls application."""

    def test_index_view(self):
        """Test that the index view loads successfully."""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)

    def test_admin_view_requires_login(self):
        """Test that admin view requires authentication."""
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 302)  # Redirect to login
