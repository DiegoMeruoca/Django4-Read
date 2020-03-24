from django.shortcuts import render
from .models import Transacao  # Importa o model

def listagem(request):
    data = {}  # Cria um dicionário vazio
    data["transacoes"] = Transacao.objects.all()  # objects é um manager pronto
    # do Django que nos permitirá acessar os dados de determinado model
    return render(request, "contas/listagem.html", data)

def home(request):
    return render(request, "contas/home.html")
'''Retorna um render permitindo renderizar um template , passando
como parametrosa request e o nome e caminho do template '''
