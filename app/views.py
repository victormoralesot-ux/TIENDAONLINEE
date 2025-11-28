from django.shortcuts import render
from .models import Insumo

def index(request):
    insumos = Insumo.objects.all()
    data = {'insumos': insumos}
    return render(request, 'index.html', data)
