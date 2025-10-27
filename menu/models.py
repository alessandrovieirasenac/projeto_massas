from django.db import models

# Create your models here.

class Reserva(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    qtd = models.IntegerField()
    data = models.DateField()
    def __str__(self):
        return f"{self.nome} - {self.telefone} - {self.email} - {self.qtd} - {self.data}"