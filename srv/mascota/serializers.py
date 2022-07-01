from rest_framework import serializers
from core.models import Producto

class Productoserializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields =['nombre','precio','descripcion']