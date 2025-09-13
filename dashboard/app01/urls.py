from django.urls import path
from .views import *

urlpatterns = [
    path("", app01, name="app01"),
    path("app01_1", app01_1, name="app01_1"), #newline
]
