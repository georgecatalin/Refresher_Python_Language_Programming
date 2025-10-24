from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index_page"),
    path("<int:month>",views.monthly_challenge_int),
    path("<str:month>", views.monthly_challenge, name="new_challenge_path")
]