from django.urls import path

from core import api

urlpatterns = [path("", api.calculate, name="calculate"),
               path("health/", api.health_check, name="health_check")]
