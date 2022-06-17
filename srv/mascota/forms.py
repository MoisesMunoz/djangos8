from django import forms
from mascota.models import PerfilUsuario, Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model=Producto
        fields='__all__'

class PerfilUsuarioForm(forms.ModelForm):
    
    class Meta:
        model=PerfilUsuario
        fields=["rut","nombre","apellido"]