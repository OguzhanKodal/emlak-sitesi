from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import kiralikTakip, kiralikDetay, kiralikResim
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.core.files import File
import uuid
from django.contrib.auth.decorators import login_required
from .models import kFavoriler
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SearchForm


def kiralik_listesi(request):
    if request.method == 'POST':
        silinecek = request.POST['sil']
        if request.user.is_superuser == False :
            return redirect("anasayfa")
        kiralikTakip.objects.get(id=silinecek).delete()
        kiralikResim.objects.filter(ilan_id=silinecek).delete()
    
    kiralikEv = kiralikTakip.objects.all().prefetch_related('resimler')  # Değiştirilen satır
    
    kiraliksablon = loader.get_template('kiralikList.html')
    kiralikVeri = {
        'kiralikEv': kiralikEv,
    }
    return HttpResponse(kiraliksablon.render(kiralikVeri, request))

@csrf_exempt
def knewilan(request):
    if request.user.is_superuser == False :
        return redirect("anasayfa")
    
    hatalar = []
    bilgi = {'new_ilan': False, 'hatalistesi': hatalar}
    
    if request.method == 'POST':
        il = request.POST.get('ili', '')
        if len(il) < 2:
            hatalar.append("Ad 2 karakterden küçük olamaz!")
        ilce = request.POST.get('ilcesi', '')
        if len(ilce) < 2:
            hatalar.append("Soyad 2 karakterden küçük olamaz!")
        mahalle = request.POST.get('mahallesi', '')
        if len(mahalle) < 2:
            hatalar.append("Soyad 2 karakterden küçük olamaz!")

        apartman = request.POST.get('apartmani', '')
        if len(apartman) < 2:
            hatalar.append("Ad 2 karakterden küçük olamaz!")

        apartmanNo = request.POST.get('apartmanNosu', '')
        if not apartmanNo.isdigit():
            hatalar.append("Apartman numarası boş olamaz!")

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
            knewilan = kiralikTakip.objects.create(
                ilanNo=ilanNo, sokak=sokak, fiyat=fiyat,
                odaSayi=odaSayi, m2=m2, aktiflik=aktiflik, il=il, 
                ilce=ilce, apartman=apartman, apartmanNo=apartmanNo, mahalle=mahalle
            )
            
            # Resimleri kaydet
            for resim in resimler:
                resim_name = f"{uuid.uuid4().hex}{resim.name[resim.name.rfind('.'):]}"
                kiralikResim.objects.create(ilan=knewilan, resim=File(resim))
            
            bilgi['new_ilan'] = True
        else:
            bilgi['hatalistesi'] = hatalar
    
    sablon = loader.get_template('kilanEkle.html')
    return HttpResponse(sablon.render(bilgi, request))

def kevDetay(request, ilanNo):
    kullanici = kiralikTakip.objects.get(id=ilanNo)
    kiralik_detaylar = kiralikDetay.objects.filter(kullanici=kullanici).first()

    detay = {
        'kiralik': kullanici,
        'kiralik_detay': kiralik_detaylar,
    }
    
    dsablon = loader.get_template('kevDetay.html')
    return HttpResponse(dsablon.render(detay, request))




def kevDuzenle(request, ilanNo):
    if request.user.is_superuser == False :
        return redirect("anasayfa")

    kiralik = kiralikTakip.objects.get(id=ilanNo)

    guncellendimi = "False"

    if request.method == 'POST':

        kiralik.sokak = request.POST.get('sokagi', '')
        kiralik.ilanNo = request.POST.get('ilanNosu', '')
        kiralik.il = request.POST.get('ili', '')
        kiralik.ilce = request.POST.get('ilcesi', '')
        kiralik.apartman = request.POST.get('apartmani', '')
        kiralik.apartmanNo = request.POST.get('apartmanNosu', '')
        kiralik.fiyat = request.POST.get('fiyati', '')
        kiralik.odaSayi = request.POST.get('odaSayisi', '')
        kiralik.m2 = request.POST.get('m2si','')
        kiralik.mahalle = request.POST.get('mahallesi', '')
        aktiflik = request.POST.get('aktiflik', False)
        if aktiflik == "on":
            kiralik.aktiflik = True
        else:
            kiralik.aktiflik = False

        kiralik.save()

        guncellendimi = "True"

    duzenle = {'kiralik': kiralik, 'guncellendimi': guncellendimi,
               'ilan_id': ilanNo}

    sablon = loader.get_template('kduzenle.html')
    return HttpResponse(sablon.render(duzenle, request))

def kdetayEkle (request, ilanNo):
    if request.user.is_superuser == False :
        return redirect("anasayfa")

    kiralik = kiralikTakip.objects.get(id=ilanNo)
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
        aciklama = request.POST.get('aciklama', '')

        yeniDetay = kiralikDetay(binaYas=binaYas, katSayi=katSayi, kat=kat, isitma=isitma,
                                otopark=otopark, ilanTarih=ilanTarih, 
                                tapuDurum=tapuDurum, esya=esya, aciklama=aciklama,
                                asonsor=asonsor,balkon=balkon,aidat=aidat, kullanici=kiralik)
        yeniDetay.save()

        guncellendimi = "True"

    ekle = {'kiralik': kiralik, 'guncellendimi': guncellendimi}

    sablon = loader.get_template('kdetayEkle.html')
    return HttpResponse(sablon.render(ekle, request))



@login_required
def kfavori_ekle(request, ilan_id):
    if request.user.is_authenticated == False :
        return redirect("anasayfa")
    ilan = get_object_or_404(kiralikTakip, id=ilan_id)
    kfavori, created = kFavoriler.objects.get_or_create(kullanici=request.user, kiralik_ilan=ilan)
    if created:
        return redirect('kfavori_listesi')
    else:
        return redirect('kevDetay', ilanNo=ilan.id)
    
def kfavori_listesi(request):
    if request.user.is_authenticated == False :
        return redirect("anasayfa")
    if request.method == 'POST':
        silinecek = request.POST['sil']
        kFavoriler.objects.get(id=silinecek).delete()  
    kfavoriler = kFavoriler.objects.filter(kullanici=request.user).select_related('kiralik_ilan')
    context = {
        'kfavoriler': kfavoriler
    }
    return render(request, 'kfavori_listesi.html', context)


def ksearch(request):
    form = SearchForm()
    results = kiralikTakip.objects.all()
    if request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            min_fiyat = form.cleaned_data['min_fiyat']
            max_fiyat = form.cleaned_data['max_fiyat']

            if query:
                results = results.filter(sokak__icontains=query)
            if min_fiyat is not None:
                results = results.filter(fiyat__gte=min_fiyat)
            if max_fiyat is not None:
                results = results.filter(fiyat__lte=max_fiyat)
    return render(request, 'ksearch_results.html', {'form': form, 'results': results})


def kilan_detay(request, ilan_id):
    kiralik = get_object_or_404(kiralikTakip, id=ilan_id)
    kiralik_detay = get_object_or_404(kiralikDetay, ilan=kiralik)  
    return render(request, 'kevDetay.html', {'kiralik': kiralik, 'kiralik_detay': kiralik_detay})
