from django.db import models

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=255)
    opcion1 = models.CharField(max_length=255)
    opcion2 = models.CharField(max_length=255)
    opcion3 = models.CharField(max_length=255)
    opcion4 = models.CharField(max_length=255)
    respuesta = models.CharField(max_length=255)

    def __str__(self):
        return self.pregunta
