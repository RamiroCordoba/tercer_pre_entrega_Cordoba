from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, "ninaApp/index.html")


def cliente(request):
    return render(request, "ninaApp/clientes.html")


def maceta(request):
    return render(request, "ninaApp/macetas.html")


def mate(request):
    contexto = {"Mates": Mate.objects.all()}
    return render(request, "ninaApp/mates.html", contexto)


def quienesSomos(request):
    return render(request, "ninaApp/quienesSomos.html")
