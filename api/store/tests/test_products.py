from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker
from store import models
import pytest

@pytest.mark.django_db
class TestGetProducts:
    
    def test_if_user_is_anonymous_returns_200(self):
        client =  APIClient()
        response = client.get('/api/products/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_is_not_staff_returns_200(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.get('/api/products/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_is_staff_returns_200(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.get('/api/products/')
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestCreateProduct:

    def test_if_user_is_anonymous_returns_401(self):
        client =  APIClient()
        response = client.post('/api/products/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_403(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.post('/api/products/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_staff_returns_201(self):
        category = baker.make(models.Category)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/api/products/', {
            'title': 'a title',
            'description': 'test description',
            'unit_price': 19.5,
            'quantity': 10,
            'category': category.pk
        })
        assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
class TestUpdateProduct:

    def test_if_user_is_anonymous_returns_401(self):
        product = baker.make(models.Product)
        client =  APIClient()
        response = client.patch(f'/api/products/{product.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_403(self):
        product = baker.make(models.Product)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.patch(f'/api/products/{product.id}/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_staff_returns_200(self):
        product = baker.make(models.Product)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.patch(f'/api/products/{product.id}/', {
            'title': 'updated title'
        })
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestDeleteProduct:

    def test_if_user_is_anonymous_returns_401(self):
        product = baker.make(models.Product)
        client =  APIClient()
        response = client.delete(f'/api/products/{product.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_403(self):
        product = baker.make(models.Product)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.delete(f'/api/products/{product.id}/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_staff_returns_204(self):
        product = baker.make(models.Product)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.delete(f'/api/products/{product.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT