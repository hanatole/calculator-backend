from core import api
from django.urls import path

urlpatterns = [path("", api.calculate, name="calculate")]
