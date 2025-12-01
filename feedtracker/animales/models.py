from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    nombre_cientifico = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    temperamento = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre
