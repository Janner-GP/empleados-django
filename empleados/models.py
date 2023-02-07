from django.db import models
from cargos.models import Cargo 
from areas.models import Area

# Create your models here.
class Empleado(models.Model):

    nombreEmpleado = models.CharField(verbose_name="Nombre", max_length=150, blank=False, null=False)
    apellidoEmpleado = models.CharField(verbose_name="Apellido", max_length=150, blank=False, null=False)
    fullnameEmpleado = models.CharField(verbose_name="Nombre Completo", max_length=150, blank=False, null=False)
    cargo = models.ForeignKey(Cargo, verbose_name="Cargo", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)

    def __str__(self):
        return str(self.cargo.Area.nombreArea)    
