from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=False,null=False)
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True,max_length=100,blank=True,null=True)
    direccion = models.CharField(max_length=100,blank=True,null=True)
    activo = models.IntegerField()

    def __str__(self):
        return str(self.nombre_usuario)
