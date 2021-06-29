from django.shortcuts import render
from django.http.response import HttpResponse
import random


# Create your views here.
def home(request): 
    return render(request,'ejercicio/home.html',{'nombre':'Darwin Gonzalez'})

def nueva(request):
    return render(request ,'ejercicio/nuevapagina.html')

def create_password(request):
    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHYJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        caracteres.extend(list('123456789'))
    if request.GET.get('special'):
        caracteres.extend(list('!"#$%&/()=?¡'))
    length = int(request.GET.get('length',8))
    pswd = ''
    for x in range(length):
        pswd += random.choice(caracteres)
    return render(request,'ejercicio/password.html',{'password':pswd})