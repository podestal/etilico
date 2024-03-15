from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker
from store import models
from django.conf import settings
import pytest

@pytest.mark.django_db
class TestGetCustomers:
    
    def test_if_user_is_anonymous_returns_401(self):
        client =  APIClient()
        response = client.get('/api/customers/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_anonymous_me_returns_401(self):
        client =  APIClient()
        response = client.get('/api/customers/me/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_200(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.get('/api/customers/')
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_is_staff_returns_200(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.get('/api/customers/')
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestCreateCustomer:

    def test_if_user_is_anonymous_returns_401(self):
        client =  APIClient()
        response = client.post('/api/customers/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_201(self):
        user = baker.make(settings.AUTH_USER_MODEL)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.post('/api/customers/', {
            'user': user.pk,
            'phone': '9085255111',
        })
        assert response.status_code == status.HTTP_201_CREATED

    def test_if_user_is_staff_returns_201(self):
        user = baker.make(settings.AUTH_USER_MODEL)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/api/customers/', {
            'user': user.pk,
            'phone': '9085255111',
        })
        assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
class TestUpdateProduct:

    def test_if_user_is_anonymous_returns_401(self):
        customer = baker.make(models.Customer)
        client =  APIClient()
        response = client.patch(f'/api/customers/{customer.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_200(self):
        customer = baker.make(models.Customer)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.patch(f'/api/customers/{customer.id}/', {
            "phone": "9085255111",
        })
        assert response.status_code == status.HTTP_200_OK

    def test_if_user_is_staff_returns_200(self):
        customer = baker.make(models.Customer)
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.patch(f'/api/customers/{customer.id}/', {
            "phone": "9085255111",
        })
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestDeleteProduct:

    def test_if_user_is_anonymous_returns_401(self):
        customer = baker.make(models.Customer)
        client =  APIClient()
        response = client.delete(f'/api/customers/{customer.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_staff_returns_403(self):
        customer = baker.make(models.Customer)
        client =  APIClient()
        client.force_authenticate(user=User(is_staff=False))
        response = client.delete(f'/api/customers/{customer.id}/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_staff_returns_204(self):
        customer = baker.make(models.Customer)
        client =  APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.delete(f'/api/customers/{customer.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
