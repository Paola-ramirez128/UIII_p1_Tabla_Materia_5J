from django.shortcuts import render, redirect
from .models import Producto

def inicio_vista(request):
    losproductos = Producto.objects.all()
    return render(request, "gestionarProducto.html", {"misproductos": losproductos})

def registrarProducto(request):
    id_producto = request.POST['txtid_producto']
    precio = request.POST['txtprecio']
    diseno = request.POST["txtdiseno"]
    fecha_entrega = request.POST['txtfecha_entrega']
    cantidad = request.POST['numcantidad']
    
    tamano = request.POST['txttamano']

    guardarProducto = Producto.objects.create(
        id_producto=id_producto, precio=precio, diseno=diseno,
        fecha_entrega=fecha_entrega, cantidad=cantidad,tamano=tamano
    )

    return redirect("/")

def seleccionarProducto(request, id_producto):  # Corregido el nombre del parámetro
    producto = Producto.objects.get(id_producto=id_producto)  # Corregido el nombre del parámetro
    return render(request, "editarproducto.html", {"misproductos": producto})

def editarProducto(request):  # También corregí un error de tipografía en el nombre de la función
    id_producto = request.POST['txtid_producto']
    precio = request.POST['txtprecio']
    diseno = request.POST['txtdiseno']
    fecha_entrega = request.POST['txtfecha_entrega']
    cantidad = request.POST['numcantidad']
    
    tamano = request.POST['txttamano']
    producto = Producto.objects.get(id_producto=id_producto)
    producto.precio = precio
    producto.diseno = diseno
    producto.fecha_entrega = fecha_entrega
    
    producto.cantidad = cantidad
    
    producto.tamano = tamano
    producto.save()  # guardar registro actualizado
    return redirect("/")

def borrarProducto(request, id_producto):  # Corregido el nombre del parámetro
    producto = Producto.objects.get(id_producto=id_producto)  # Corregido el nombre del parámetro
    producto.delete()
    return redirect("/")
