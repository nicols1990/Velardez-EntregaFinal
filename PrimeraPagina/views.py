from django.shortcuts import render, redirect
from django.http import HttpResponse
from PrimeraPagina.forms import CreacionProducto
from PrimeraPagina.models import Producto
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


def inicio(request):
   # return HttpResponse("hola")
   return render(request, "PrimeraPagina/inicio.html")

#Esto es para crear el template(plantilla)
@login_required
def crear_producto(request):
   
   print("Estos son los datos del POST", request.GET)
   print("Estos son los datos del POST", request.POST)
   
   if request.method =="POST":
      formulario= CreacionProducto(request.POST)
      if formulario.is_valid():
         info=formulario.cleaned_data
         #aca crea el auto en la vista
         producto=Producto(codigo=info.get("codigo"),descripcion=info.get("descripcion"),fecha=info.get("fecha"))
         #aca lo guarda en la base de datos
         producto.save()
         return redirect("lista_de_productos")
   else:
      formulario= CreacionProducto()
      
   
   return render(request, "PrimeraPagina/crear_producto.html", {"formulario": formulario})


def lista_de_productos(request):
   productos=Producto.objects.all()
   return render(request, "PrimeraPagina/lista_de_productos.html", {"productos":productos}) # esto es para que se vea la lista de prodcutos en el html que hay que ubicar los mismo  


def detalle_producto(request, producto_en_especifico):
   producto= Producto.objects.get(id=producto_en_especifico)
   return render(request, "PrimeraPagina/detalle_producto.html", {"producto":producto})


#Clases Basadas en vistas
class VistaDetalleProducto(DetailView):
   model= Producto
   template_name= "PrimeraPagina/detalle_producto.html"
   
   
#El longin que esta como atributo hace que si no esta logiado, no te deja modificar, importante el orden en que se lo ponga
class VistaModificarProducto(LoginRequiredMixin, UpdateView):
   model= Producto
   template_name= "PrimeraPagina/modificar_producto.html"
   fields=["codigo", "descripcion","fecha"]
   success_url= reverse_lazy("lista_de_productos")
   
#El longin que esta como atributo hace que si no esta logiado, no te deja eliminar, importante el orden en que se lo ponga
class VistaEliminarProducto(LoginRequiredMixin, DeleteView,):
   model= Producto
   template_name= "PrimeraPagina/eliminar_producto.html"
   success_url= reverse_lazy("lista_de_productos")
   