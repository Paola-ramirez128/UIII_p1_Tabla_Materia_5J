from django.urls import path
from producto_app import views

urlpatterns = [
    path("producto", views.inicio_vistaProductos, name="producto"),
    path("registrarProdcuto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<codigo>",views.seleccionarProducto,name="seleccionarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto"),
    path("borrarProducto/<codigo>",views.borrarProducto,name="borrarProducto")

]
