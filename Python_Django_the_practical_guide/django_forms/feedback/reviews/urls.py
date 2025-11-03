from django.urls import path
from . import views

urlpatterns = [
    path("", views.display),
    path("thank-you",views.display_thank, name="thank-you-page")
]
