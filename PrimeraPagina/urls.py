from django.urls import path
from PrimeraPagina.views import inicio, crear_producto, lista_de_productos


urlpatterns = [
    path("" ,inicio, name="inicio"),
    path("productos/crear/", crear_producto, name="crear_producto"),
    path("productos/", lista_de_productos ,name="lista_de_productos")
]