from django.http import HttpResponse, request
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 

def anasayfa(request):
    sablon = loader.get_template('index.html')
    return HttpResponse(sablon.render(request = request))