from django import forms
from .models import Producto,Pedido


class Formproducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
        

class Formpedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'