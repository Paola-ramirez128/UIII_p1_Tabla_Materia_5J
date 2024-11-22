from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    pedidos=models.IntegerField()
    fecha_registro=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre