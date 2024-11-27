from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.
def inicio_vista(request):
    losclientes=Cliente.objects.all()
    return render(request,"gestionarClientes.html",{"misclientes":losclientes})


def registrarClientes(request):
    id_cliente=request.POST["txtid_cliente"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]
    correo=request.POST["txtcorreo"]
    pedidos=request.POST["numpedidos"]
    fecha_registro=request.POST["txtfecha_registro"]

    guardarCliente=Cliente.objects.create(
        id_cliente=id_cliente,nombre=nombre,telefono=telefono,direccion=direccion,correo=correo,pedidos=pedidos,fecha_registro=fecha_registro
    )#GUARDAR EL REGISTRO

    return redirect("/")

def seleccionarClientes(request,id_cliente):
    clientes=Cliente.objects.get(id_cliente=id_cliente)
    return render(request,"editarclientes.html",{"misclientes":clientes})

def editarClientes(request):
    id_cliente=request.POST["txtid_cliente"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]
    correo=request.POST["txtcorreo"]
    pedidos=request.POST["numpedidos"]
    fecha_registro=request.POST["txtfecha_registro"]
    clientes=Cliente.objects.get(id_cliente=id_cliente)
    clientes.nombre=nombre
    clientes.telefono=telefono
    clientes.direccion=direccion
    clientes.correo=correo
    clientes.pedidos=pedidos
    clientes.fecha_registro=fecha_registro
    clientes.save() #guarda registro actualizado
    return redirect("/")

def borrarClientes(request,id_cliente):
    clientes=Cliente.objects.get(id_cliente=id_cliente)
    clientes.delete() #borra el resgistro
    return redirect("/")