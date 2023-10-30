import random
import json
import bson
from rest_framework import status


def mock_add_user_and_cities_to_user_collection(data):
    return str(bson.ObjectId())


def mock_add_user_cities_to_cities_collection(data):
    pass


def mock_get_user_cities_percentage(user_id=None):
    return 100* random.random()


def test_receive_user_and_cities_view(api_client, monkeypatch, fake):
    request_data = {
        "user_id": fake.password(length=12),
        "cities": [fake.ean(length=8)[:-1] for _ in range(random.randint(10, 100))]
    }

    monkeypatch.setattr(
        "nba_fantasy_analyzer.usecases.add_user_and_cities_to_user_collection", mock_add_user_and_cities_to_user_collection
    )
    monkeypatch.setattr(
        "nba_fantasy_analyzer.usecases.add_user_cities_to_cities_collection", mock_add_user_cities_to_cities_collection
    )

    response = api_client.post(
        f"/api/v1/add_cities/", data=request_data, format="json"
    )

    response_data = response.json()
    _id = response_data.pop("_id")

    assert response.status_code == status.HTTP_201_CREATED
    assert response_data == request_data
    assert type(_id) == str


def test_get_user_percentage_of_completeness_and_city_data_view(api_client, monkeypatch, fake):
    request_data = {
        "user_id": f"{fake.password(length=12)}"
    }

    monkeypatch.setattr(
        "nba_fantasy_analyzer.api.v1.views.get_user_cities_percentage", mock_get_user_cities_percentage
    )

    response = api_client.generic(
        method="GET",
        path="/api/v1/get_cities/",
        data=json.dumps(request_data),
        content_type="application/json"
    )

    response_data = response.json()
    percentage = response_data.pop("percentage")

    assert response.status_code == status.HTTP_200_OK
    assert response_data == request_data
    assert type(percentage) == str
    assert float(percentage)
