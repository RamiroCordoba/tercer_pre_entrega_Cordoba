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


def mateForm(request):
    if request.method == "POST":
        miForm = MateForm(request.POST)
        if miForm.is_valid():
            mate_nombre = miForm.cleaned_data.get("nombre")
            mate_tamaño = miForm.cleaned_data.get("tamaño")
            mate_descripcion = miForm.cleaned_data.get("descripcion")
            mate_stock = miForm.cleaned_data.get("stock")
            mate_precio = miForm.cleaned_data.get("precio")
            mateNuevo = Mate(
                nombre=mate_nombre,
                tamaño=mate_tamaño,
                descripcion=mate_descripcion,
                stock=mate_stock,
                precio=mate_precio,
            )
            mateNuevo.save()
            contexto = {"Mate": Mate.objects.all()}
            return render(request, "ninaApp/mates.html", contexto)
    else:
        miForm = MateForm()
    return render(request, "ninaApp/mateForm.html", {"form": miForm})


def clienteForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_email = miForm.cleaned_data.get("email")
            cliente_telefono = miForm.cleaned_data.get("telefono")
            clienteNuevo = Cliente(
                nombre=cliente_nombre,
                apellido=cliente_apellido,
                email=cliente_email,
                telefono=cliente_telefono,
            )
            clienteNuevo.save()
            contexto = {"Clientes": Cliente.objects.all()}
            return render(request, "ninaApp/clientes.html", contexto)
    else:
        miForm = ClienteForm()
    return render(request, "ninaApp/clienteForm.html", {"form": miForm})


# _____________ Buscar
def buscarMacetas(request):
    return render(request, "ninaApp/buscar.html")


def encontrarMacetas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        macetas = Maceta.objects.filter(nombre__icontains=patron)
        contexto = {"Macetas": macetas}
        return render(request, "ninaApp/macetas.html", contexto)
    contexto = {"Maceta": Maceta.objects.all()}
    return render(request, "ninaApp/macetas.html", contexto)
