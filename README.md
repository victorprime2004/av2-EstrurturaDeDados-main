# ------------------------------------ERRO 1----------------------------------------------
    # ERRO 1 ENCONTRADO: Não estava sendo importado o 'timezone'
    # CORREÇÃO DO ERRO 1: O 'timezone' foi importado, estava dando erro porque o 'timezone' não estava sendo importado

# ------------------------------------ERRO 2----------------------------------------------
    # ERRO 2 ECONTRADO: O erro era, porque  estava repetindo a pasta 'template'. E isso fazia o Djnago pensar que tinha outra pasta 'template' dentro da pasta 'portal'. E não existe 
    # CORREÇÃO DO ERRO 2: A pasta 'template' ja estava integrada na pasta 'portal', ou seja não precisava repetir a pasta 'template' no caminho.

# ------------------------------------ERRO 3----------------------------------------------
    # ERRO 3 ENCONTRADO: O erro era que a classe Professor não estava sendo importada da maneira incorreta: from models import Professor
    # CORREÇÃO DO ERRO 3: A alteração foi na forma de importação: from portal.models import Professor, que anteriomente estava sendo feita incorretamente.

# ------------------------------------ERRO 4----------------------------------------------
    # ERRO 4 ENCONTRADO: O erro era, porque estava contendo texto dentro de urlpatterns, e isso não permitido, o Djnago precisa entender que é uma URL, e não um texto.
    # CORREÇÃO DO ERRO 4: A alteração que foi feita foi, retirar o texto que estava dentro de urlppatterns, e colocar include('portal.urls').

# ------------------------------------ERRO 5----------------------------------------------
    # ERRO 5 ENCONTRADO: Estava campo 'especialidade' que não existe na classe Professor.
    # CORREÇÃO DO ERRO 5: O campo 'especialidade' foi substituído pelo campo 'discplina'.

# ------------------------------------ERRO 6----------------------------------------------
    # ERRO 6 ENCONTRADO: O 'portal' não foi adicionado, por isso o Django não reconhece ele e os outros arquivos que estão dentro dele.
    # CORREÇÃO DO ERRO 6: A alteraççao feita foi que a pasta 'portal' foi adicionado, porque o Django precisa reconhecer que existe um aplicativo chamado 'portal'

# ------------------------------------ERRO 7----------------------------------------------
    # ERRO 7 ENCONTRADO: Estava com IntegerField.
    # CORREÇÃO DO ERRO 7: O campo 'matricula' dever ser CharField, pois pode conter letras e números, e não apenas números.

# ------------------------------------ERRO 8----------------------------------------------
    # ERRO 8 ENCONTRADO: A view  'cadastro' não existe. E o erro era, porque estava tentando chamar a view 'cadastro' que não existe.
    # CORREÇÃO DO ERRO 8: Eu deletei a linha que estava tentando chamar a view 'cadastro', porque ela não existe na views.py.


# Instrução de como rodar o projeto localmente
python -m pip install django pillow
python manage.py migrate
python manage.py runserver