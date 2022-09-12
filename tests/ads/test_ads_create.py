import pytest

from ads.models.ad import Ad


@pytest.mark.django_db
def test_create_ad(client, user_token):
    expected_response = {
        "id": 1,
        "author": None,
        "category": None,
        "name": "test_from_test",
        "price": 100,
        "description": None,
        "is_published": False,
        "image": None
    }

    data = {
        "name": "test_from_test",
        "price": 100
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer " + user_token)

    assert response.status_code == 201
    assert response.data == expected_response
