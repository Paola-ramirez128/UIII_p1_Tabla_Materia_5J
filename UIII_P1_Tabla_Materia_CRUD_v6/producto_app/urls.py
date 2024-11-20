from django.urls import path
from producto_app import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarProdcuto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<codigo>",views.seleccionarProducto,name="seleccionarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto"),
    path("borrarProducto/<codigo>",views.borrarProducto,name="borrarProducto")

]
