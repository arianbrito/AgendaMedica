from django.db import models
from django.contrib.auth.models import User
from medico.models import DatasAbertas

# Classe do objeto de status - criação de tabelas no sql
class Consulta(models.Model):
    status_choices = (
        ('A', 'Agendada'),
        ('F', 'Finalizada'),
        ('C', 'Cancelada'),
        ('I', 'Iniciada')
    )

    paciente = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_aberta = models.ForeignKey(DatasAbertas, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=status_choices, default='A')
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.paciente.username
    
# Classe do objeto Documento - criação de tabelas no sql 
class Documento(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=50)
    documento = models.FileField(upload_to='documentos')

    def __str__(self):
        return self.titulo