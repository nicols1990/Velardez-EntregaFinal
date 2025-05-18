from django.urls import path
from PrimeraPagina.views import inicio, crear_producto, lista_de_productos,detalle_producto,VistaDetalleProducto, VistaModificarProducto, VistaEliminarProducto


urlpatterns = [
    path("" ,inicio, name="inicio"),
    path("productos/", lista_de_productos ,name="lista_de_productos"),
    path("productos/crear/",crear_producto, name="crear_producto"),
    path("productos/<int:producto_en_especifico>/",detalle_producto,name="detalle_producto"), #se pasa como variables para guardar la id
    path("productos/<int:pk>/",VistaDetalleProducto.as_view(),name="detalle_producto"),
    path("productos/<int:pk>/modificar", VistaModificarProducto.as_view(),name="modificar_producto"),
    path("productos/<int:pk>/eliminar/", VistaEliminarProducto.as_view(),name="eliminar_producto"),
]