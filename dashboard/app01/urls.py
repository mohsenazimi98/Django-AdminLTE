from django.urls import path
from .views import app01

urlpatterns = [
    path("", app01, name="app01"),
]
