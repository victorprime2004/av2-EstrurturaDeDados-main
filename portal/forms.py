from django import forms

from portal.models import Professor  # ERRO 3 ENCONTRADO: O erro era que a classe Professor não estava sendo importada da maneira incorreta: from models import Professor

                                    # CORREÇÃO DO ERRO 3: A alteração foi na forma de importação: from portal.models import Professor, que anteriomente estava sendo feita incorretamente.

class ProfessorForm(forms.ModelForm):
    class Meta:  # A classe meta serve para configurar o form
        model = Professor  # Define o model que o form representa
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'registro',]
