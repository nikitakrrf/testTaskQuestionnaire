import pytest
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
# Create your tests here.

pytestmark = pytest.mark.django_db

def test_real_answer():
    client = APIClient()

    url = reverse('questions:questions-check', kwargs={"pk": 777})
    test_one = client.post(url, {"user_id": "demo_id", "text": "test"}, format='json')
    assert test_one.status_code == 404

