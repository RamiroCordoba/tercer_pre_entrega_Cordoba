from django.urls import path, include
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("cactus/", cactus, name="cactus"),
    path("macetas/", maceta, name="macetas"),
    path("clientes/", cliente, name="clientes"),
]
