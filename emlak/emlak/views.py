from django.http import HttpResponse, request
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def anasayfa(request):
    sablon = loader.get_template('index.html')
    return HttpResponse(sablon.render(request = request))

def hakkinda(request):
    sablon = loader.get_template('hakkinda.html')
    return HttpResponse(sablon.render(request = request))

def iletisim(request):
    sablon = loader.get_template('iletisim.html')
    return HttpResponse(sablon.render(request = request))


# views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def iletisim_gonder(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("anasayfa")   
    bilgi = {}

    if request.method == 'POST':
        kullaniciadi = request.POST['username']
        sifre = request.POST['password']
        kullanici = authenticate(request, username=kullaniciadi, password=sifre)

        if kullanici is not None:
            login(request, kullanici)
            return redirect("anasayfa")
        else:
            bilgi['login'] = 'Hata'

    sablon = loader.get_template('login.html')
    return HttpResponse(sablon.render(bilgi, request))

def user_logout(request):
    logout(request)
    return redirect("anasayfa")
def user_register(request):
    sablon = loader.get_template('register.html')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            kullaniciadi = form.cleaned_data["username"]
            sifre = form.cleaned_data["password1"]
            kullanici = authenticate(request, username=kullaniciadi,
                                    password=sifre)
            login(request, kullanici)
            return redirect("anasayfa")
        else:
            bilgi = {"form" : form}
            return HttpResponse(sablon.render(bilgi, request))
    form = UserCreationForm()
    bilgi = {"form": form}
    return HttpResponse(sablon.render(bilgi, request))