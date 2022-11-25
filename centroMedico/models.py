from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Paciente(models.Model):
  nombre = models.CharField (max_length = 24, verbose_name = 'Nombre')
  apellido = models.CharField(max_length = 24, verbose_name = 'Apellido')
  email = models.EmailField(max_length = 60, verbose_name = 'Email')
  contraseña = models.CharField(max_length = 24, verbose_name = 'Contraseña')

  def __str__(self):
    return self.nombre