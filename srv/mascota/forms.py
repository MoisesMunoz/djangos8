from django import forms
from mascota.models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model=Producto
        fields='__all__'