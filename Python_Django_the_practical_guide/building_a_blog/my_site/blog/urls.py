from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_page, name="start_page"),
    path("posts/", views.list_posts, name="list_page"),
    path("posts/<slug:slug>/",views.detail_post, name="detail_page")
]
