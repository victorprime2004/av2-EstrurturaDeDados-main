from jango.shortcuts import render

# GET, POST, PUT, DELETE
# REQUEST <-> RESPONSE
# RENDER -> RENDERIZAR

# CRIANDO UMA VIEW PARA APRESENTAR A PÁGINA INDEX - USE FUNÇÃO
def index(request):  # É a request feita pelo usuário
    return render(
        request,
        'portal/index.html'  # ERRO 2 ECONTRADO: O erro era, porque  estava repetindo a pasta 'template'. E isso fazia o Djnago pensar que tinha outra pasta 'template' dentro da pasta 'portal'. E não existe 

        #CORREÇÃO DO ERRO 2: A pasta 'template' ja estava integrada na pasta 'portal', ou seja não precisava repetir a pasta 'template' no caminho.
     )
