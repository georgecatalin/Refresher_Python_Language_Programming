from django.urls import path
from . import views

urlpatterns = [
    path("",views.index ),
    path("<slug:slug>", views.get_detail,name="detail-book")
]
