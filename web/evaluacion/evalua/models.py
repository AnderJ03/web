from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):

    user = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.EmailField()


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Empresa(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    correo = models.EmailField()
    telefono = models.IntegerField()
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
             return self.nombre
        
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

class Bus(models.Model):
     capacidad = models.IntegerField()
     num_bus = models.IntegerField()
     estado = models.BooleanField(default=True)    
     climatizado = models.IntegerField()
     fk_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

     def __str__(self):
          return str(self.num_bus)
     
     class meta:
          verbose_name = 'Bus'
          verbose_name_plural = 'Buses'

class Ruta(models.Model):
     region =models.CharField(max_length=50)
     descripcion = models.TextField()

     def __str__(self):
          return self.region
     
     class meta:
          verbose_name = 'Ruta'
          verbose_name_plural = 'Rutas'


class Viaje(models.Model):
     origen = models.CharField(max_length=45)
     destino = models.CharField(max_length=45)
     fecha_hora = models.DateTimeField()
     precio = models.FloatField()
     clase = models.CharField(max_length=45)
     cupo = models.CharField(max_length=45)
     fk_ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
     fk_bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

     def __str__(self):
          return self.origen
     
     class meta:
          verbose_name = 'Viaje'
          verbose_name_plural = 'Viajes'

def url_perfil(self, filename):
    ruta = "static/img/perfiles/%s/%s/"%(self.usuario, str(filename))
    return ruta

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    direccion = models.TextField()
    cedula = models.CharField(max_length=10)
    foto = models.ImageField(upload_to=url_perfil)
    USERNAME_FIELD = "username"

    def foto_perfil(self):
        return mark_safe('<a href="/%s"target="_blank"><img src="/%s" width="50px" heigth="50px" ></a>' % (self.foto, self.foto))
        
    foto_perfil.allow_tags = True

    class meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'


    def __str__(self):
        return self.usuario.username
        

             

