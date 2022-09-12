import pytest

from ads.models.ad import Ad


@pytest.fixture()
@pytest.mark.django_db
def user_token(client, django_user_model):
    """Create user and Get JWT token"""
    username = "fixture-user"
    password = "123fixture"

    django_user_model.objects.create_user(
        username=username, password=password)

    response = client.post(
        "/user/token/",
        {"username": username, "password": password},
        format="json"
    )

    return response.data["access"]
