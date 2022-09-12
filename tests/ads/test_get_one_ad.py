import pytest


@pytest.mark.django_db
def test_get_one_ad(client, ad, user_token):
    expected_response = {
        "id": ad.pk,
        "author": None,
        "category": None,
        "image": None,
        "name": ad.name,
        "price": ad.price,
        "description": None,
        "is_published": False
    }

    response = client.get(
        f"/ad/{ad.pk}/",
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    assert response.status_code == 200
    assert response.data == expected_response