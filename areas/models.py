from django.db import models

# Create your models here.
class Area(models.Model):
    nombreArea = models.CharField(max_length=80, unique=True, blank=False, null=False)
    descripcionArea = models.CharField(max_length=250)

    def __str__(self):
        return self.nombreArea