from django.db import models


class Catalog(models.Model):
    nombre = models.CharField(max_length=30)



