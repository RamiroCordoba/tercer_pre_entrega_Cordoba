from django import forms


class MacetaForm(forms.Form):
    nombre = forms.CharField(max_length=20, required=True)
    tamaño = forms.IntegerField(required=True)
    descripcion = forms.CharField(max_length=2000, required=False)
    stock = forms.IntegerField(required=True)
    precio = forms.DecimalField(max_digits=6, decimal_places=2, required=True)
