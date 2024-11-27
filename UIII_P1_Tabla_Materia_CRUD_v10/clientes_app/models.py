from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=20)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=20)
    correo=models.CharField(max_length=20)
    pedidos=models.PositiveSmallIntegerField(max_length=10)
    fecha_registro=models.CharField(max_length=20)