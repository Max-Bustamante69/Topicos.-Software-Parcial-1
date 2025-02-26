from django.db import models

# Create your models here.
class Vuelo(models.Model):
    OPCIONES_TIPO = [('Nacional', 'Nacional'),('Internacional', 'Internacional')]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=OPCIONES_TIPO)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.nombre} ({self.tipo})'
    
    
    