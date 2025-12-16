from django.shortcuts import render,get_object_or_404
from .models import Producto, Categoria, Pedido, Insumo
from app.forms import Formproducto,Formpedido
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InsumoSerializer
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render


class insumos_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    
class insumos_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

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


from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render
from .models import Pedido

@login_required
def reporte_pedidos(request):
    pedidos = Pedido.objects.all()

    
    fecha_inicio = request.GET.get("fecha_inicio")
    fecha_fin = request.GET.get("fecha_fin")

    if fecha_inicio and fecha_fin:
        pedidos = pedidos.filter(creado__date__range=[fecha_inicio, fecha_fin])

    
    pedidos_por_estado = pedidos.values("estado").annotate(total=Count("id"))

    
    pedidos_por_plataforma = pedidos.values("red_social").annotate(total=Count("id"))

    context = {
        "pedidos_por_estado": pedidos_por_estado,
        "pedidos_por_plataforma": pedidos_por_plataforma,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
    }

    return render(request, "reporte_pedidos.html", context)

