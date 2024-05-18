from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class satilikTakip(models.Model):
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

class satilikResim(models.Model):
    ilan = models.ForeignKey(satilikTakip, on_delete=models.CASCADE, related_name='resimler')
    resim = models.ImageField(upload_to='satilik_images/')
       
class satilikDetay(models.Model):
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
    kullanici = models.ForeignKey(satilikTakip, on_delete = models.CASCADE,
                                  related_name = 'kullanici', null=True)
    

    def __str__(self):
        return f"{self.binaYas} {self.katSayi} {self.kat} {self.isitma}"


class Favoriler(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kullanici_favori')
    satilik_ilan = models.ForeignKey(satilikTakip, on_delete=models.CASCADE, related_name='favori_ilan')
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('kullanici', 'satilik_ilan')

    def __str__(self):
        return f"{self.kullanici.username} - {self.satilik_ilan.ilanNo}"