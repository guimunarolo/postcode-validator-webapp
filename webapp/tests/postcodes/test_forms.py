from apps.postcodes.forms import PostcodeValidationForm
from postcode_validator_uk.validators import UKPostcode


def test_postcode_validation_form_postcode_is_required():
    form = PostcodeValidationForm({"postcode": None})

    assert form.is_valid() is False
    assert form.errors["postcode"] == ["This field is required."]


def test_postcode_validation_form_validated():
    form = PostcodeValidationForm({"postcode": "EC1A 1BB"})

    assert form.is_valid() is True
    assert isinstance(form.cleaned_data["postcode"], UKPostcode) is True


def test_postcode_validation_form_return_validation_error():
    form = PostcodeValidationForm({"postcode": "14020680"})

    assert form.is_valid() is False
    assert "postcode" in form.errors
