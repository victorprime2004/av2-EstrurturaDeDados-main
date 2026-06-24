from django.urls import path

from portal import views

# exemplo: path('index/', views.index)
urlpatterns = [
    path('index/', views.index),
      # ERRO 8 ENCONTRADO: A view  'cadastro' não existe. E o erro era, porque estava tentando chamar a view 'cadastro' que não existe.

      # CORREÇÃO DO ERRO 8: Eu deletei(comentei) a linha , porque ela não existe na views.py.

]


# Verbos HTTP - FRONTEND <-> BACKEND
#  GET -> www.escola.com -> Exiba a página home da escola.
#  POST -> www.escola.com/cadastro -> Cadastrando um novo usuário.
#  PUT -> www.escola.com/logado/alterar/1 -> Alterando o dado do usuário.
#  DELETE -> www.escola.com/logado/deletar/1 -> Deletando um usuário.
