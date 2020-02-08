import pytest
import status
from apps.postcodes.forms import PostcodeValidationForm
from django.test import Client
from django.urls import reverse


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def postcode_validation_endpoint():
    return reverse("postcode_validation")


def test_postcode_validation_view_renderization(client, postcode_validation_endpoint):
    response = client.get(postcode_validation_endpoint)

    assert response.status_code == status.HTTP_200_OK
    assert response.template_name == ["validation.html"]
    assert isinstance(response.context_data["form"], PostcodeValidationForm) is True


def test_postcode_validation_view_post_invalid_postcode(client, postcode_validation_endpoint):
    response = client.post(postcode_validation_endpoint, {"postcode": "wrong"})
    form = response.context_data["form"]

    assert response.status_code == status.HTTP_200_OK
    assert "postcode" in form.errors


def test_postcode_validation_view_post_valid_postcode(client, postcode_validation_endpoint):
    response = client.post(postcode_validation_endpoint, {"postcode": "EC1A 1BB"})

    expected_postcode_data_keys = [
        "validated_postcode",
        "raw_postcode",
        "outward",
        "inward",
        "area",
        "district",
        "sector",
        "unit",
    ]

    assert response.status_code == status.HTTP_200_OK
    assert list(response.context_data["postcode_data"].keys()) == expected_postcode_data_keys
