from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker
from store import models
import pytest

@pytest.mark.django_db
class TestGetCategories:
    
    def test_if_user_is_anonymous_returns_200(self):
        client =  APIClient()
        response = client.get('/api/categories/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_is_not_staff_returns_200(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.get('/api/categories/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_is_staff_returns_200(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.get('/api/categories/')
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestCreateCategory:

    def test_if_user_is_anonymous_returns_401(self):
        client =  APIClient()
        response = client.post('/api/categories/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_403(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.post('/api/categories/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_staff_returns_201(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/api/categories/', {
            'title': 'a title',
        })
        assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
class TestUpdateCategory:

    def test_if_user_is_anonymous_returns_401(self):
        category = baker.make(models.Category)
        client =  APIClient()
        response = client.patch(f'/api/categories/{category.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_403(self):
        category = baker.make(models.Category)
        client =  APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.patch(f'/api/categories/{category.id}/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_staff_returns_200(self):
        category = baker.make(models.Category)
        client =  APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.patch(f'/api/categories/{category.id}/', {
            'title': 'updated title'
        })
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestDeleteCategory:

    def test_if_user_is_anonymous_returns_401(self):
        category = baker.make(models.Category)
        client =  APIClient()
        response = client.delete(f'/api/categories/{category.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_403(self):
        category = baker.make(models.Category)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.delete(f'/api/categories/{category.id}/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_staff_returns_204(self):
        category = baker.make(models.Category)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.delete(f'/api/categories/{category.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT