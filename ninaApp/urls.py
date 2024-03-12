from django.urls import path, include
from .views import *

urlpatterns = [
    # _________ Menu principal
    path("", home, name="home"),
    path("mates/", mate, name="mates"),
    path("macetas/", maceta, name="macetas"),
    path("clientes/", cliente, name="clientes"),
    # ________ Otras paginas
    path("quienesSomos/", quienesSomos, name="quienes_somos"),
    # ________ Formularios
    path("maceta_form/", macetaForm, name="maceta_form"),
]
