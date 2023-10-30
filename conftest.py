import pytest
from faker import Faker

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def api_client_with_credentials(user, api_client):
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)


@pytest.fixture
def fake():
    return Faker("en")


@pytest.fixture
def cities_data():
    return ["1234567", "1234568", "1234569", "1234567"]
