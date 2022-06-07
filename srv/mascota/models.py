from asyncio.windows_events import NULL
import email
from django.db import models

# Create your models here.
class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.id} - {self.nombre} {self.precio}"

class PerfilCliente(models.Model):
    nombre_usuario=models.CharField(max_length=50)

class Pedido(models.Model):
    id=models.AutoField(primary_key=True)
    fecha=models.DateField()

class Detalle(models.Model):
    id=models.AutoField(primary_key=True)