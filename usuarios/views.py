from django.shortcuts import render
from django.http import HttpResponse

def login(requst):
    return HttpResponse('login')


def cadastro(request):
    return render(request, 'cadastro.html')

