from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
