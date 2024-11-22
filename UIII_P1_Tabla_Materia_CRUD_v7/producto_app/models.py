from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto=models.CharField(primary_key=True,max_length=10)
    precio=models.CharField(max_length=20)
    diseno=models.CharField(max_length=20)
    fecha_entrega=models.CharField(max_length=20)
    cantidad=models.PositiveSmallIntegerField()
    fecha_elaboracion=models.CharField(max_length=20)
    tamano=models.CharField(max_length=20)
    def __str__(self):
        return self.precio