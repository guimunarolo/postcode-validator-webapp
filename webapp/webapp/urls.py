from django.urls import include, path

urlpatterns = [
    path("", include("apps.postcodes.urls")),
]
