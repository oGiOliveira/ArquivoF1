from django.db import models
from django.db.models import Sum 

#Tabela de Pilotos:
class Piloto(models.Model):
    nome= models.CharField(max_length=100)
    equipe= models.CharField(max_length=100)
    dataNasc= models.DateField()
    numeracao= models.IntegerField()
    pais= models.CharField(max_length=100)
    foto= models.ImageField(upload_to='systemDrivers')

    def __str__(self):
        return '|Piloto: ' + self.nome + ' |Equipe: ' + self.equipe + ' |Numeração: ' + str(self.numeracao)

    class Meta:
        verbose_name = 'Piloto'
        verbose_name_plural = 'Pilotos'
        ordering = ['id']
