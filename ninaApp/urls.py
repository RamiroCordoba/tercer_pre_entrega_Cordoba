from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("mates/", mate, name="mates"),
    path("macetas/", maceta, name="macetas"),
    path("clientes/", cliente, name="clientes"),
    path("quienesSomos/", quienesSomos, name="quienes_somos"),
]
