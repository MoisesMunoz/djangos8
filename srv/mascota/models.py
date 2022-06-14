from asyncio.windows_events import NULL
import email
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
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