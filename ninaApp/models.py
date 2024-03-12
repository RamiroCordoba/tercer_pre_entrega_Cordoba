from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)


class Maceta(models.Model):
    nombre = models.CharField(max_length=20)
    tamaño = models.IntegerField()
    descripcion = models.TextField(blank=True)
    stock = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=6, decimal_places=2)


class Cactus(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)


class Planta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    tieneFlor = models.BooleanField(default=False)
