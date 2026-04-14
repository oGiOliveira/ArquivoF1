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

'''
#Tabel de Equipes:
class Equipe(models.Model):
    nomeE= models.CharField(max_length=100)
    paisE= models.CharField(max_length=100)
    vitorias= models.IntegerField()
    best_time= models.IntegerField()
    bestP= models.CharField(max_length=100) #usar outra coisa no CharField

#Tabela de Pistas:
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

#desenvolva seus modelos aqui. Tipo isso:





######################################

class Formulario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transfers')
    tipoForm = models.CharField(max_length=20, default='despesa')
    nomeForm = models.CharField(max_length=100)
    valorForm = models.DecimalField(max_digits=10, decimal_places=2)
    dataForm = models.DateField()
    descricaoForm = models.TextField(blank = True, null = True)


    #nomeando no admin o form para que não fique object(1), object(2)...
    def __str__(self):
        return '|Formulario: ' + self.nomeForm + ' |Descricao: ' + self.descricaoForm + ' |Usuario: ' + self.usuario.username
    
    #numerando os formularios no admin
    class Meta: 
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'
        ordering = ['id']
'''
