from django.contrib import admin
from .models import kiralikTakip, kiralikResim, kiralikDetay, kFavoriler

class kiralikResimInline(admin.TabularInline):
    model = kiralikResim

class kiralikDetayInline(admin.TabularInline):
    model = kiralikDetay

@admin.register(kiralikTakip)
class kiralikTakipAdmin(admin.ModelAdmin):
    inlines = [kiralikResimInline, kiralikDetayInline]
    list_display = ("ilanNo", "il","ilce","apartman","apartmanNo",
                    "mahalle", "sokak", "fiyat", "aktiflik", "odaSayi", "m2")
    empty_value_display = "BOŞ"

@admin.register(kiralikDetay)
class kiralikDetayAdmin(admin.ModelAdmin):
    list_display = ("binaYas", "katSayi", "kat", "isitma", 
                    "otopark", "ilanTarih", "tapuDurum", "esya", 
                    "asonsor", "balkon", "aidat","aciklama")
    empty_value_display = "BOŞ"


@admin.register(kFavoriler)
class kFavorilerAdmin(admin.ModelAdmin):
    list_display = ('kullanici', 'kiralik_ilan', 'eklenme_tarihi')
    list_filter = ('kullanici',)
    search_fields = ('kullanici__username', 'kiralik_ilan__ilanNo')

