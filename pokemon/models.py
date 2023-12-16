from django.db import models

# Create your models here.

class Pokemon(models.Model):
    Nombre = models.CharField(max_length=25)
    Numero = models.IntegerField()
    Generacion = models.CharField(max_length=27, default='')
    Tipo = models.CharField(max_length=30, default='')