from django import forms
from .models import Producto


class Formproducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'