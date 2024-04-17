from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import satilikTakip, satilikDetay
from django.views.decorators.csrf import csrf_exempt

def satilik_listesi(request):
    if request.method == 'POST':
        silinecek = request.POST['sil']
        satilikTakip.objects.get(id = silinecek).delete()
    satilikEv = satilikTakip.objects.all().values()
    satiliksablon = loader.get_template('satilikList.html')
    satilikVeri = {
        'satilikEv' : satilikEv
    }
    return HttpResponse(satiliksablon.render(satilikVeri,request))


@csrf_exempt
def newilan(request):
    if request.user.is_authenticated == False :
        return redirect("anasayfa")
    bilgi = {'yeniKayit': "False"}

    if request.method == 'POST':
        ilanNo = request.POST.get('ilanNosu', '')
        sokak = request.POST.get('sokagi', '')
        fiyat = request.POST.get('fiyati', '')
        odaSayi = request.POST.get('odaSayisi', '')
        m2 = request.POST.get('m2si', '')

        aktiflik = request.POST.get('aktiflik', False)
        if aktiflik == "on":
            aktiflik = True

        newilan = satilikTakip(ilanNo=ilanNo, sokak=sokak, fiyat=fiyat,
                                 odaSayi=odaSayi, m2 = m2,
                                aktiflik=aktiflik)
        newilan.save()
        bilgi = {'newilan': "True"}

    newilansablon = loader.get_template('ilanEkle.html')
    return HttpResponse(newilansablon.render(bilgi, request))


def evDetay(request, ilanNo):
    kullanici = satilikTakip.objects.get(id=ilanNo)
    satiliklar = satilikDetay.objects.filter(kullanici=kullanici)
    evler = satilikDetay.objects.filter(kullanici=kullanici)

    detay = {'daire': kullanici,'satililiklar':satiliklar,
             'evler' : evler}

    dsablon = loader.get_template('evDetay.html')
    return HttpResponse(dsablon.render(detay, request))


def evDuzenle(request, ilanNo):
    if request.user.is_authenticated == False :
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
    if request.user.is_authenticated == False :
        return redirect("anasayfa")

    satilik = satilikTakip.objects.get(id=ilanNo)
    guncellendimi = "False"
    if request.method == 'POST':

        binaYas = request.POST.get('binaYasi', '')
        katSayi= request.POST.get('katSayisi', '')
        kat = request.POST.get('kati', '')        
        isitma= request.POST.get('isitmasi', '')
        otopark = request.POST.get('otoparki', '')       
        ilanTarih= request.POST.get('ilanTarihi', '')
        tapuDurum = request.POST.get('tapudurumu', '')
        esya = request.POST.get('esyalimi', '')
        asonsor= request.POST.get('asonsormu', '')
        balkon = request.POST.get('balkonmu', '')
        aidat = request.POST.get('aidati', '')

        yeniDetay = satilikDetay(binaYas=binaYas, katSayi=katSayi, kat=kat, isitma=isitma,
                                otopark=otopark, ilanTarih=ilanTarih, 
                                tapuDurum=tapuDurum, esya=esya, 
                                asonsor=asonsor,balkon=balkon,aidat=aidat)
        yeniDetay.save()

        guncellendimi = "True"

    ekle = {'satilik': satilik, 'guncellendimi': guncellendimi,
            'ilan_id': ilanNo}

    sablon = loader.get_template('detayEkle.html')
    return HttpResponse(sablon.render(ekle, request))


