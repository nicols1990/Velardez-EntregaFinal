from django import forms

#creamos el formulario
class CreacionProducto(forms.Form):
    codigo=forms.CharField (max_length=20)
    descripcion=forms.CharField(max_length=20)
    
    #es una mascara para la vista de la pagina (widget=forms.DateField(attrs={"type":"date"}
    fecha=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))