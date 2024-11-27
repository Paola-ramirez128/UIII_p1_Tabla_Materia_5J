from django.shortcuts import render,redirect
from .models import Materia
# Create your views here.
def inicio_vistaMateria(request):
    lasmaterias=Materia.objects.all()
    return render(request,"gestionarMateria.html",{"mismaterias":lasmaterias})


def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]

    guardarMateria=Materia.objects.create(
        codigo=codigo,nombre=nombre,creditos=creditos
    )#GUARDAR EL REGISTRO

    return redirect("/")

def seleccionarMateria(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    return render(request,"editarmateria.html",{"mismaterias":materia})

def editarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]
    materia=Materia.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.creditos=creditos
    materia.save() #guarda registro actualizado
    return redirect("/")

def borrarMateria(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    materia.delete() #borra el resgistro
    return redirect("/")

    