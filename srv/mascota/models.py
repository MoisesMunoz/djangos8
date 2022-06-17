from asyncio.windows_events import NULL
import email
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

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

class PerfilCliente(models.Model):
    nombre_usuario=models.OneToOneField(User, on_delete=models.CASCADE)

class Pedido(models.Model):
    id=models.AutoField(primary_key=True)
    fecha=models.DateField()

class Detalle(models.Model):
    id=models.AutoField(primary_key=True)