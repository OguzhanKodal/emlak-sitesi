from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import satilikTakip, satilikDetay, satilikResim
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.core.files import File
import uuid
from django.contrib.auth.decorators import login_required
from .models import Favoriler
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


def satilik_listesi(request):
    if request.method == 'POST':
        silinecek = request.POST['sil']
        if request.user.is_superuser == False :
            return redirect("anasayfa")
        satilikTakip.objects.get(id=silinecek).delete()
        satilikResim.objects.filter(ilan_id=silinecek).delete()
    
    satilikEv = satilikTakip.objects.all().prefetch_related('resimler')  # Değiştirilen satır
    
    satiliksablon = loader.get_template('satilikList.html')
    satilikVeri = {
        'satilikEv': satilikEv,
    }
    return HttpResponse(satiliksablon.render(satilikVeri, request))

@csrf_exempt
def newilan(request):
    if request.user.is_superuser == False :
        return redirect("anasayfa")
    
    hatalar = []
    bilgi = {'new_ilan': False, 'hatalistesi': hatalar}
    
    if request.method == 'POST':
        sokak = request.POST.get('sokagi', '')
        if len(sokak) < 2:
            hatalar.append("Ad 2 karakterden küçük olamaz!")
        
        odaSayi = request.POST.get('odaSayisi', '')
        if len(odaSayi) < 2:
            hatalar.append("Soyad 2 karakterden küçük olamaz!")
        
        resimler = request.FILES.getlist('daireResmi')
        
        ilanNo = request.POST.get('ilanNosu', '')
        if not ilanNo.isdigit() or int(ilanNo) < 0:
            hatalar.append("Üye no boş veya negatif olamaz!")
        
        m2 = request.POST.get('m2si', '')
        if not m2.isdigit():
            hatalar.append("m2 boş olamaz!")
        
        fiyat = request.POST.get('fiyati', '')
        if not fiyat.isdigit():
            hatalar.append("Fiyat boş olamaz!")
                
        aktiflik = request.POST.get('aktiflik', False)
        if aktiflik == "on":
            aktiflik = True
        
        if not hatalar:
            newilan = satilikTakip.objects.create(
                ilanNo=ilanNo, sokak=sokak, fiyat=fiyat,
                odaSayi=odaSayi, m2=m2, aktiflik=aktiflik
            )
            
            # Resimleri kaydet
            for resim in resimler:
                resim_name = f"{uuid.uuid4().hex}{resim.name[resim.name.rfind('.'):]}"
                satilikResim.objects.create(ilan=newilan, resim=File(resim))
            
            bilgi['new_ilan'] = True
        else:
            bilgi['hatalistesi'] = hatalar
    
    sablon = loader.get_template('ilanEkle.html')
    return HttpResponse(sablon.render(bilgi, request))

def evDetay(request, ilanNo):
    kullanici = satilikTakip.objects.get(id=ilanNo)
    satilik_detaylar = satilikDetay.objects.filter(kullanici=kullanici).first()

    detay = {
        'satilik': kullanici,
        'satilik_detay': satilik_detaylar,
    }
    
    dsablon = loader.get_template('evDetay.html')
    return HttpResponse(dsablon.render(detay, request))




def evDuzenle(request, ilanNo):
    if request.user.is_superuser == False :
        return redirect("anasayfa")

    satilik = satilikTakip.objects.get(id=ilanNo)

    guncellendimi = "False"

    if request.method == 'POST':

        satilik.sokak = request.POST.get('sokagi', '')
        satilik.fiyat = request.POST.get('fiyati', '')
        satilik.odaSayi = request.POST.get('odaSayisi', '')
        satilik.m2 = request.POST.get('m2si','')
        aktiflik = request.POST.get('aktiflik', False)
        if aktiflik == "on":
            satilik.aktiflik = True
        else:
            satilik.aktiflik = False

        satilik.save()

        guncellendimi = "True"

    duzenle = {'satilik': satilik, 'guncellendimi': guncellendimi,
               'ilan_id': ilanNo}

    sablon = loader.get_template('duzenle.html')
    return HttpResponse(sablon.render(duzenle, request))

def detayEkle (request, ilanNo):
    if request.user.is_superuser == False :
        return redirect("anasayfa")

    satilik = satilikTakip.objects.get(id=ilanNo)
    guncellendimi = "False"
    if request.method == 'POST':

        binaYas = request.POST.get('binaYas', '')
        katSayi= request.POST.get('katSayi', '')
        kat = request.POST.get('kat', '')        
        isitma= request.POST.get('isitma', '')
        otopark = request.POST.get('otopark', '')       
        ilanTarih= request.POST.get('ilanTarih', '' )
        tapuDurum = request.POST.get('tapuDurum', '')
        esya = request.POST.get('esya', '')
        asonsor= request.POST.get('asonsor', '')
        balkon = request.POST.get('balkon', '')
        aidat = request.POST.get('aidat', '')

        yeniDetay = satilikDetay(binaYas=binaYas, katSayi=katSayi, kat=kat, isitma=isitma,
                                otopark=otopark, ilanTarih=ilanTarih, 
                                tapuDurum=tapuDurum, esya=esya, 
                                asonsor=asonsor,balkon=balkon,aidat=aidat, kullanici=satilik)
        yeniDetay.save()

        guncellendimi = "True"

    ekle = {'satilik': satilik, 'guncellendimi': guncellendimi}

    sablon = loader.get_template('detayEkle.html')
    return HttpResponse(sablon.render(ekle, request))



@login_required
def favori_ekle(request, ilan_id):
    if request.user.is_authenticated == False :
        return redirect("anasayfa")
    ilan = get_object_or_404(satilikTakip, id=ilan_id)
    favori, created = Favoriler.objects.get_or_create(kullanici=request.user, satilik_ilan=ilan)
    if created:
        return redirect('favori_listesi')
    else:
        return redirect('evDetay', ilanNo=ilan.id)
    
def favori_listesi(request):
    if request.user.is_authenticated == False :
        return redirect("anasayfa")
    if request.method == 'POST':
        silinecek = request.POST['sil']
        Favoriler.objects.get(id=silinecek).delete()  
    favoriler = Favoriler.objects.filter(kullanici=request.user).select_related('satilik_ilan')
    context = {
        'favoriler': favoriler
    }
    return render(request, 'favori_listesi.html', context)
