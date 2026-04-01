from django.db import models

#desenvolva seus modelos aqui. Tipo isso:
'''
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
