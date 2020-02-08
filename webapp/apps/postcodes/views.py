from django.views.generic import FormView

from .forms import PostcodeValidationForm


class PostcodeValidationView(FormView):
    template_name = "validation.html"
    form_class = PostcodeValidationForm

    def form_valid(self, form):
        postcode = form.cleaned_data["postcode"]
        postcode_data = {
            "validated_postcode": postcode.validated_postcode,
            "raw_postcode": postcode.raw_postcode,
            "outward": postcode.outward,
            "inward": postcode.inward,
            "area": postcode.area,
            "district": postcode.district,
            "sector": postcode.sector,
            "unit": postcode.unit,
        }

        return self.render_to_response(self.get_context_data(postcode_data=postcode_data))
