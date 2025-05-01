from django import forms

#creamos el formulario
class CreacionProducto(forms.Form):
    codigo=forms.CharField (max_length=20)
    descripcion=forms.CharField(max_length=20)