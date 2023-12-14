from django.db import models

# Create your models here.

class Reserva(models.Model):
    id_reserva      = models.AutoField(primary_key=True)
    fecha           = models.DateTimeField()
    nombre          = models.CharField(max_length=30)
    email           = models.CharField(max_length=35)
    comentarios     = models.CharField(max_length=100)
    
    def __str__(self):
        return "ID: "+str(self.id_reserva)