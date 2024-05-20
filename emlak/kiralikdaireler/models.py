from django.db import models
from django.contrib.auth.models import User

class kiralikTakip(models.Model):
    ilanNo = models.IntegerField(null=True)
    il = models.CharField(max_length=20)
    ilce = models.CharField(max_length=20)
    mahalle = models.CharField(max_length=20)
    sokak = models.CharField(max_length=20)
    apartman = models.CharField(max_length=20)
    apartmanNo = models.IntegerField(null=True)
    fiyat = models.IntegerField(null=True)
    m2 = models.IntegerField(null=True)  
    aktiflik = models.BooleanField(null=True)
    odaSayi = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.ilanNo} {self.sokak} {self.fiyat} {self.m2}"

class kiralikResim(models.Model):
    ilan = models.ForeignKey(kiralikTakip, on_delete=models.CASCADE, related_name='resimler')
    resim = models.ImageField(upload_to='kiralik_images/')
       
class kiralikDetay(models.Model):
    binaYas = models.IntegerField(null=True)  
    katSayi = models.IntegerField(null=True)  
    kat = models.IntegerField(null=True)  
    isitma = models.CharField(max_length=20)
    ilanTarih = models.DateField(null=True)
    tapuDurum = models.CharField(max_length=20)
    esya = models.CharField(max_length=20)
    asonsor = models.CharField(max_length=20)
    balkon = models.CharField(max_length=20)
    otopark = models.CharField(max_length=20)
    aidat = models.IntegerField(null=True)
    aciklama = models.TextField(null=True)
    kullanici = models.ForeignKey(kiralikTakip, on_delete = models.CASCADE,
                                  related_name = 'kullanici', null=True)
    

    def __str__(self):
        return f"{self.binaYas} {self.katSayi} {self.kat} {self.isitma}"


class kFavoriler(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kiralik_kullanici_favori')
    kiralik_ilan = models.ForeignKey(kiralikTakip, on_delete=models.CASCADE, related_name='kiralik_favori_ilan')
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('kullanici', 'kiralik_ilan')

    def __str__(self):
        return f"{self.kullanici.username} - {self.kiralik_ilan.ilanNo}"
