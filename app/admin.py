from django.contrib import admin
from .models import producto
from .models import categoria
from .models import insumo

# Register your models here.


@admin.register(producto)
class RifaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'categoria', 'precio_base', 'imagenes')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre', 'descripcion')

@admin.register(categoria)
class RifaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
