from django.db import models
from areas.models import Area

# Create your models here.
class Cargo(models.Model):
    nombreCargo = models.CharField(max_length=70, unique=True, blank=False, null=False)
    descripcionCargo = models.CharField(max_length=250)
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreCargo
    