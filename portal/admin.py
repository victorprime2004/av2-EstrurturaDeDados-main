from django.contrib import admin
from portal import models

@admin.register(models.Professor)  # Registrando a classe Professor no Portal do Django
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'disciplina', 'ativo',)  # ERRO 5 ENCONTRADO: Estava campo 'especialidade' que não existe na classe Professor.
                                                                    # CORREÇÃO DO ERRO 5: O campo 'especialidade' foi substituído pelo campo 'discplina'.
@admin.register(models.Aluno)  # Registrando a classe Aluno no Portal do Django
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Aula)  # Registrando a classe Aula no Portal do Django
class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno_id', 'professor_id', 'status',)
