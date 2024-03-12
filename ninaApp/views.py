from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, "ninaApp/index.html")


def cliente(request):
    return render(request, "ninaApp/clientes.html")


def maceta(request):
    return render(request, "ninaApp/macetas.html")


def cactus(request):
    contexto = {"Cactus": Cactus.objects.all()}
    return render(request, "ninaApp/cactus.html", contexto)
