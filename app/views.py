from django.shortcuts import render,get_object_or_404
from .models import Producto, Categoria, Pedido, Insumo
from app.forms import Formproducto,Formpedido
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InsumoSerializer
from rest_framework import status

def index(request):
    buscar = request.GET.get("buscar", "")
    precio_base = request.GET.get("precio_base", "")   
    categoria_id = request.GET.get("categoria", "")

    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    if buscar:
        productos = productos.filter(nombre__icontains=buscar)

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    if precio_base:
        productos = productos.filter(precio_base__lte=precio_base)  

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

def seguimiento_pedido(request, token):
    pedido = get_object_or_404(Pedido, token_seguimiento=token)
    return render(request, "seguimiento.html", {"pedido": pedido})

def api_productos(request):
    api ={'id':1,'nombre':'Producto','precio_base':100}
    return JsonResponse(api)

def insumos(request):
    insumos = Insumo.objects.all()
    data ={'insumos': list(insumos.values('nombre','cantidad_disponible','unidad','marca','color'))}
    return JsonResponse(data)

@api_view(['GET','POST'])
def insumos_list(request):
    if request.method == 'GET':
        insumos = Insumo.objects.all()
        ser = InsumoSerializer(insumos, many=True)
        return Response(ser.data)
    
    if request.method == 'POST':
        ser = InsumoSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)


@api_view(['GET','PUT','DELETE'])
def insumos_detail(request, pk):
    pass