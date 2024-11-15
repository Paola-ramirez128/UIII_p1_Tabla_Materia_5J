from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.
def inicio_vista(request):
    losproductos=Producto.objects.all()
    return render(request,"gestionaProducto.html",{"misproductos":losproductos})

def registrarProducto(request):
    id_producto=request.POST["txtcodigo"]
    precio=request.POST["txtprecio"]
    diseno=request.POST["txtdiseno"]
    fecha_entrega=request.POST["txtfecha_entrga"]
    cantidad=request.POST["numcantidad"]
    fecha_elaboracion=request.POST["txtfecha_elaboracion"]
    tamano=request.POST["txttamano"]

    guardarProducto=Producto.objects.create(
        id_producto=id_producto,precio=precio,diseno=diseno,fecha_entrega=fecha_entrega,cantidad=cantidad,fecha_elaboracion=fecha_elaboracion,tamano=tamano
    )#GUARDAR EL REGISTRO
    return redirect("/")

def seleccionarProducto(request,id_prodcuto):
    producto=Producto.objects.get(id_prodcuto=id_prodcuto)
    return render(request,"editarproducto.html",{"misproductos":producto})

def editarProducto(request):
    id_producto=request.POST["txtcodigo"]
    precio=request.POST["txtprecio"]
    diseno=request.POST["txtdiseno"]
    fecha_entrega=request.POST["txtfecha_entrga"]
    cantidad=request.POST["numcantidad"]
    fecha_elaboracion=request.POST["txtfecha_elaboracion"]
    tamano=request.POST["txttamano"]
    producto=Producto.objects.get(id_producto=id_producto)
    producto.precio=precio
    producto.diseno=diseno
    producto.fecha_entrega=fecha_entrega
    producto.cantidad=cantidad
    producto.fecha_elaboracion=fecha_elaboracion
    producto.tamano=tamano
    producto.save() #guarda registro actualizado
    return redirect("/")

def borrarProducto(request,id_producto):
    producto=Producto.objects.get(id_producto=id_producto)
    producto.delete() #borra el resgistro
    return redirect("/")
