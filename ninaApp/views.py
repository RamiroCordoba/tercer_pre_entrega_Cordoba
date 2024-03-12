from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request, "ninaApp/index.html")


def cliente(request):
    contexto = {"Clientes": Cliente.objects.all()}
    return render(request, "ninaApp/clientes.html", contexto)


def maceta(request):
    contexto = {"Macetas": Maceta.objects.all()}
    return render(request, "ninaApp/macetas.html", contexto)


def mate(request):
    contexto = {"Mates": Mate.objects.all()}
    return render(request, "ninaApp/mates.html", contexto)


def quienesSomos(request):
    return render(request, "ninaApp/quienesSomos.html")


# _________ Form ___________


def macetaForm(request):
    if request.method == "POST":
        miForm = MacetaForm(request.POST)
        if miForm.is_valid():
            maceta_nombre = miForm.cleaned_data.get("nombre")
            maceta_tamaño = miForm.cleaned_data.get("tamaño")
            maceta_descripcion = miForm.cleaned_data.get("descripcion")
            maceta_stock = miForm.cleaned_data.get("stock")
            maceta_precio = miForm.cleaned_data.get("precio")
            macetaNueva = Maceta(
                nombre=maceta_nombre,
                tamaño=maceta_tamaño,
                descripcion=maceta_descripcion,
                stock=maceta_stock,
                precio=maceta_precio,
            )
            macetaNueva.save()
            contexto = {"Maceta": Maceta.objects.all()}
            return render(request, "ninaApp/macetas.html", contexto)
    else:
        miForm = MacetaForm()
    return render(request, "ninaApp/macetaForm.html", {"form": miForm})
