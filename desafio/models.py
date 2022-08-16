from django.db import models

# Create your models here.

class Blog(models.Model):
    autor = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'Tengo un blog llamado {self.autor}'
    
