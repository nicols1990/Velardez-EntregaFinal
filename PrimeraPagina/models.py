from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=20)
    fecha=models.DateField(null=True)
    
    
def __str__(self):
    return f'{self.codigo} - {self.descripcion}'
