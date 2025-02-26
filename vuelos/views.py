from django.shortcuts import render, redirect
from django.db.models import Avg
from .forms import VueloForm
from .models import Vuelo

def index(request):
    return render(request, 'home.html')

def registrar_vuelo(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vuelos')
        
        
    else:
        form = VueloForm()
    return render(request, 'registrar_vuelo.html', {'form': form})

def listar_vuelos(request):
    
    return render(request, 'listar_vuelos.html', {'vuelos': Vuelo.objects.all()})

def estadisticas_vuelos(request):
    vuelos_nacionales = Vuelo.objects.filter(tipo='Nacional').count()
    vuelos_internacionales = Vuelo.objects.filter(tipo='Internacional').count()
    precio_promedio_nacionales = Vuelo.objects.filter(tipo='Nacional').aggregate(Avg('precio'))['precio__avg']
    
    context = {
        'vuelos_nacionales': vuelos_nacionales,
        'vuelos_internacionales': vuelos_internacionales,
        'precio_promedio_nacionales': precio_promedio_nacionales,
    }
    return render(request, 'estadisticas_vuelos.html', context)

