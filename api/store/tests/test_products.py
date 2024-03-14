from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestGetProducts:
    pass

# def test_if_user_anonymus_returns_200(self):
# # Arrange

# # Act
# client = APIClient()
# response = client.get('/api/services/')
# # Assert
# assert response.status_code == status.HTTP_200_OK