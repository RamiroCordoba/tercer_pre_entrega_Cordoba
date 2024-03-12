from django.contrib import admin
from .models import *

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "telefono")
    list_filter = ("nombre", "apellido")


class MacetaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tamaño", "descripcion", "stock", "precio")
    list_filter = ("nombre", "tamaño", "stock", "precio")


class MateAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tamaño", "descripcion", "stock", "precio")
    list_filter = ("nombre", "tamaño", "stock", "precio")


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Maceta, MacetaAdmin)
admin.site.register(Mate, MateAdmin)
