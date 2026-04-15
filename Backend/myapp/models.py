from django.db import models
from django.db.models import Sum 

class Equipe(models.Model):
    nomeE = models.CharField(max_length=100)
    paisE = models.CharField(max_length=100)
    vitorias = models.IntegerField(default=0)
    best_time = models.CharField(max_length=100, blank=True, null=True)
    bestP = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nomeE  # Mostra o nome da equipe no admin
    
    def atualizar_stats(self):
        # Pega todos os pilotos desta equipe
        pilotos = self.piloto_set.all()
        
        # Só calcula se tiver pelo menos um piloto
        if pilotos.exists():
            # Soma todos os campeao dos pilotos
            self.vitorias = pilotos.aggregate(Sum('campeao'))['campeao__sum']
            
            melhor = pilotos.order_by('bestT').first()# Pega o piloto com menor bestT (melhor tempo)
            self.best_time = f"{melhor.nome} - {melhor.bestT}s"
            
            campeao = pilotos.order_by('-campeao').first() #Pega o piloto com maior vitorias(campeao)
            self.bestP = f"{campeao.nome} - {campeao.campeao} títulos" # e vai aparecer o nome do pilot com o tempo
            self.save()# Salva as alterações no banco

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

class Pista(models.Model):
    nomeP= models.CharField(max_length=100)
    paísP= models.CharField(max_length=100)
    vencedores= models.CharField(max_length=100)

#Tabela de Campeõs:
class Campeoes(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    vitorias = models.IntegerField(default=0)
    menor_tempo = models.DecimalField(max_digits=6, decimal_places=3)
    
    def __str__(self):
        return self.nome