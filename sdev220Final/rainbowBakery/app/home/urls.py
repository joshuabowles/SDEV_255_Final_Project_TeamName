from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.Home),
    path("stock/", views.Stock)
]
