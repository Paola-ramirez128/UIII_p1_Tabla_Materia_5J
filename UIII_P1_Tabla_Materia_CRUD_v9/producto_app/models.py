from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto=models.CharField(primary_key=True,max_length=10)
    precio=models.CharField(max_length=10)
    diseno=models.CharField(max_length=10)
    fecha_entrega=models.CharField(max_length=20)
    cantidad=models.PositiveSmallIntegerField()
    
    tamano=models.CharField(max_length=100)
    def __str__(self):
        return self.precio