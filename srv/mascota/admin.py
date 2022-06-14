from django.contrib import admin

from mascota.models import Producto

# Register your models here.
admin.site.register(Producto)

class admProducto(admin.ModelAdmin):
    list_display=["id","nombre","precio","descripcion"]
    list_editable=["nombre","precio","descripcion"]
    list_filter=["nombre","precio"]
    
    class Meta:
        model=Producto
