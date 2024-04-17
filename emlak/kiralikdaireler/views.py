from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def ilan_listesi(request):
    ilansablon = loader.get_template('kiraList.html')
    return HttpResponse(ilansablon.render())