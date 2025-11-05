from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("profiles_list/", views.UserProfilesView.as_view())
]
