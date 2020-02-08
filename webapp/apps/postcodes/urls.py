from django.urls import path

from .views import PostcodeValidationView

urlpatterns = [
    path("", PostcodeValidationView.as_view(), name="postcode_validation"),
]
