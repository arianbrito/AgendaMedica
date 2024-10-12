from django.contrib import admin
from .models import Consulta, Documento

# Register your models here.
# Registo da classe do objeto ou tabela de dados
admin.site.register(Consulta)
admin.site.register(Documento)