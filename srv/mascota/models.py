from asyncio.windows_events import NULL
import email
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Categoria_Producto(models.Model):
    id=models.AutoField(primary_key=True)
    categoria=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id} - {self.categoria}"

class Animal_Producto(models.Model):
    id=models.AutoField(primary_key=True)
    animal=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id} - {self.animal}"

class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    animal=models.ForeignKey(Animal_Producto, on_delete=models.CASCADE, default=1)
    categoria=models.ForeignKey(Categoria_Producto, on_delete=models.CASCADE, default=1)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    stock=models.IntegerField(default=0)
    imagen=models.ImageField(upload_to="productos",null=True)
    
    def __str__(self):
        return f"{self.id} - {self.nombre} {self.precio}"

class PerfilUsuario(models.Model):
    nombre_usuario=models.CharField(primary_key=True,max_length=50)
    rut=models.CharField(unique=True,max_length=12)
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    
    def __str__(self):
        return self.nombre + " " + self.apellido

class Pedido(models.Model):
    id=models.AutoField(primary_key=True)
    fecha=models.DateField()

class Detalle(models.Model):
    id=models.AutoField(primary_key=True)