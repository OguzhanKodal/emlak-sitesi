from django.db import models

# Create your models here.

class satilikTakip(models.Model):
    ilanNo = models.IntegerField(default=0)
    sokak = models.CharField(max_length=15)
    fiyat = models.IntegerField(null=True)
    m2 = models.IntegerField(null=True)  
    aktiflik = models.BooleanField(null=True)
    odaSayi = models.CharField(max_length=15)


    def __str__(self):
        return self.sokak
   
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
    kullanici = models.ForeignKey(satilikTakip, on_delete = models.CASCADE,
                                  related_name = 'kullanici', null=True)
    

    def __str__(self):
        return self.isitma

