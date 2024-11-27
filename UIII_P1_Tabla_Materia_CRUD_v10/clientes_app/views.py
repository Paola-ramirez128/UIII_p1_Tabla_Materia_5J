from django.shortcuts import render, redirect
from .models import Cliente

def inicio_vista(request):
    losclientes=Cliente.objects.all()
    return render(request,"gestionarClientes.html", {"misclientes":losclientes})

def registrarCliente(request):
    id_cliente=request.POST('txtid_cliente')
    nombre=request.POST('txtnombre')
    telefono=request.POST('numtelefono')
    direccion=request.POST('txtdireccion')
    correo=request.POST('txtcorreo')
    pedidos=request.POST('numpedidos')
    fecha_registro=request.POST('txtfecha_registro')

    guardarCliente=Cliente.objects.create(
        id_cliente=id_cliente,nombre=nombre,telefono=telefono,direccion=direccion,correo=correo,pedidos=pedidos,fecha_registro=fecha_registro
    )
    return redirect("/")

def seleccionarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    return render(request,"editarclientes.html",{"misclientes":cliente})

def editarCliente(request):
    id_cliente=request.POST('txtid_cliente')
    nombre=request.POST('txtnombre')
    telefono=request.POST('numtelefono')
    direccion=request.POST('txtdireccion')
    correo=request.POST('txtcorreo')
    pedidos=request.POST('numpedidos')
    fecha_registro=request.POST('txtfecha_registro')
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre=nombre
    cliente.telefono=telefono
    cliente.direccion=direccion
    cliente.correo=correo
    cliente.pedidos=pedidos
    cliente.fecha_registro=fecha_registro
    cliente.save()
    return redirect("/")

def borrarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("/")