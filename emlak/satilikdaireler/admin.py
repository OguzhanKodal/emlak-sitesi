from django.contrib import admin
from .models import satilikTakip
from .models import satilikDetay

# Register your models here.

class satilikTakipAdmin(admin.ModelAdmin):
    list_display = ("ilanNo", "sokak", "fiyat","aktiflik","odaSayi","m2")
    empty_value_display = "BOŞ"

class satilikDetayAdmin(admin.ModelAdmin):
    list_display = ("binaYas", "katSayi", "kat", "isitma", "otopark", 
                    "ilanTarih", "tapuDurum", "esya", "asonsor","balkon","aidat")
    empty_value_display = "BOŞ"

admin.site.register(satilikTakip, satilikTakipAdmin)
admin.site.register(satilikDetay,satilikDetayAdmin)

