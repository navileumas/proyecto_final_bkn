from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo