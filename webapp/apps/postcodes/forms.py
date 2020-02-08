from django import forms
from postcode_validator_uk.exceptions import InvalidPostcode
from postcode_validator_uk.validators import UKPostcode


class PostcodeValidationForm(forms.Form):
    postcode = forms.CharField(label="Postcode", max_length=16)

    def clean_postcode(self):
        try:
            postcode = UKPostcode(self.cleaned_data["postcode"])
            postcode.validate()
        except InvalidPostcode as exc:
            raise forms.ValidationError(f"{exc}")

        return postcode
