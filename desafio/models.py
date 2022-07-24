from django.db import models

# Create your models here.

class Blog(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'Tengo un blog llamado {self.nombre}'
    
