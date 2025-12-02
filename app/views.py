from django.shortcuts import render,get_object_or_404
from .models import Producto, Categoria, Pedido
from app.forms import Formproducto,Formpedido

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

def producto_detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto_detalle.html', {'producto': producto})

def agregar_producto(request):
    form = Formproducto()
    
    if request.method == 'POST':
        form = Formproducto(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form': form}
    return render(request, 'producto_nuevo.html',data)

def agregar_formulario(request):
    form = Formpedido()
    
    if request.method == 'POST':
        form = Formpedido(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return ver_pedidos(request)
    data = {'form': form}
    return render(request, 'formulario.html',data)

def ver_pedidos(request):
    pedidos = Pedido.objects.all()
    data = {'pedidos': pedidos}
    return render(request, 'verpedidos.html', data)

