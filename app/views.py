from django.shortcuts import render
from .models import Producto, Categoria

def index(request):
    buscar = request.GET.get("buscar", "")
    categoria_id = request.GET.get("categoria", "")

    productos = Producto.objects.all()
    categorias = Categoria.objects.all()


    if buscar:
        productos = productos.filter(nombre__icontains=buscar)


    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    data = {
        'productos': productos,
        'categorias': categorias,
        'request': request   
    }

    return render(request, 'index.html', data)

def hola(request):
    return render(request, 'hola.html')
