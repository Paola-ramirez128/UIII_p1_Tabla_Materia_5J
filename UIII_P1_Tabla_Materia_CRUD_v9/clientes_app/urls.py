from django.urls import path
from clientes_app import views

urlpatterns = [
    path("", views.inicio_vista, name="inicio_vista"),
    path("registrarClientes/",views.registrarClientes,name="registrarClientes"),
    path("seleccionarClientes/<codigo>",views.seleccionarClientes,name="seleccionarClientes"),
    path("editarClientes/",views.editarClientes,name="editarClientes"),
    path("borrarClientes/<codigo>",views.borrarClientes,name="borrarClientes")

]