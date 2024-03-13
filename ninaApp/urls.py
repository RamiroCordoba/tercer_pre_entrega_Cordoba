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
    path("mate_form/", mateForm, name="mate_form"),
    path("cliente_form/", clienteForm, name="cliente_form"),
    # _________ Busqueda
    path("buscar_macetas/", buscarMacetas, name="buscar_macetas"),
    path("encontrar_macetas/", encontrarMacetas, name="encontrar_macetas"),
]
