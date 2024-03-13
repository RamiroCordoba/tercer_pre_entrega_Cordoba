from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nombre", "apellido"]

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"


class Maceta(models.Model):
    nombre = models.CharField(max_length=20)
    tamaño = models.IntegerField()
    descripcion = models.CharField(max_length=2000, blank=True)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ["nombre"]

    def __str__(self) -> str:
        return f"{self.nombre}"


class Mate(models.Model):
    nombre = models.CharField(max_length=20)
    tamaño = models.IntegerField()
    descripcion = models.CharField(max_length=2000, blank=True)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ["nombre"]

    def __str__(self) -> str:
        return f"{self.nombre}"
