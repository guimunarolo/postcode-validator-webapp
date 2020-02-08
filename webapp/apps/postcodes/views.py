from django.views.generic import TemplateView


class PostcodeValidationView(TemplateView):
    template_name = "validation.html"
