from django import forms
from .models import Vuelo

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['nombre', 'tipo', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del vuelo'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }
