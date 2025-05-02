from django.shortcuts import render, redirect
from django.http import HttpResponse
from PrimeraPagina.forms import CreacionProducto
from PrimeraPagina.models import Producto
# Create your views here.


def inicio(request):
   # return HttpResponse("hola")
    return render(request, "PrimeraPagina/inicio.html")
 
#Esto es para crear el template(plantilla)
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