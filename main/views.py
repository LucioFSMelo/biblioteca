from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario

def home(request):
    if request.session.get('usuario'): #Ao tentar pegar uma session chamada usuário, se ela existir
        usuario = Usuario.objects.get(id = request.session['usuario']).nome # Buscando o único usuário que atende as condições.
        return HttpResponse(f'Olá {usuario}') # Devemos mostrar o sistema
    else:
        return redirect('/auth/login/?status=2') #Se não, redireciona para a página de login
