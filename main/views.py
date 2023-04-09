from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    if request.session.get('usuario'): #Ao tentar pegar uma session chamada usuário, se ela existir
        return HttpResponse('Hello') # Devemos mostrar o sistema
    else:
        return redirect('/auth/login/?status=2') #Se não, redireciona para a página de login
