from dataclasses import fields
from genericpath import exists
from .models import Categoria_Producto, PerfilUsuario, Producto, Animal_Producto
from rest_framework import serializers

class Animal_ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Animal_Producto
        fields='__all__'

class Categoria_ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria_Producto
        fields='__all__'


class ProductoSerializer(serializers.ModelSerializer):
    animal=Animal_ProductoSerializer(read_only=True)
    categoria=Categoria_ProductoSerializer(read_only=True)
    # animal_id=serializers.PrimaryKeyRelatedField(queryset=Animal_Producto.objects.all(),source="animal")
    # nombre=serializers.CharField(required=True, min_length=3)

    # def validate_nombre(self,value):
    #     existe=Producto.objects.filter(nombre__iexact=value).exists()
    #     if existe:
    #         raise serializers.ValidationError("Este producto ya existe")
    #     return value

    class Meta:
        model=Producto
        fields='__all__'

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=PerfilUsuario
        fields='__all__'