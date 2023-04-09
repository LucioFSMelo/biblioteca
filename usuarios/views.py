from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256

def login(requst):
    status = requst.GET.get('status')
    return render(requst, 'login.html', {'status': status})


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0: #Nome e email não podem ser nulos
        return redirect('/auth/cadastro/?status=1')
    
    if len(senha) < 8:  # A senha tem que ter pelo menos 8 dígitos.
        return redirect('/auth/cadastro/?status=2')
    
    if len(usuario) > 0:  # Se o usuário já estiver cadastrado, redirecione, se não, cadastrar o usuário.
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, 
                          email = email, 
                          senha = senha)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(senha = senha) #Filtrando email e senha (se são iguais)

    if len(usuario) == 0: #se o usuário não existir, volte para o login (vai ter que cadastrar)
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0: # O usuário existe (vamos redirecioná-lo para página da aplicação)
        request.session['usuario'] = usuario[0].id
        return redirect('/livros/home')
    
    return HttpResponse(f"{email} {senha}")

def sair(request):
    request.session.flush() # Para limpar a session do usuário
    return redirect('/auth/login/')


