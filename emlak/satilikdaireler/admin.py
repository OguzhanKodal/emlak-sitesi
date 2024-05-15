from django.contrib import admin
from .models import satilikTakip, satilikResim, satilikDetay, Favoriler

class satilikResimInline(admin.TabularInline):
    model = satilikResim

class satilikDetayInline(admin.TabularInline):
    model = satilikDetay

@admin.register(satilikTakip)
class satilikTakipAdmin(admin.ModelAdmin):
    inlines = [satilikResimInline, satilikDetayInline]
    list_display = ("ilanNo", "sokak", "fiyat", "aktiflik", "odaSayi", "m2")
    empty_value_display = "BOŞ"

@admin.register(satilikDetay)
class satilikDetayAdmin(admin.ModelAdmin):
    list_display = ("binaYas", "katSayi", "kat", "isitma", "otopark", "ilanTarih", "tapuDurum", "esya", "asonsor", "balkon", "aidat")
    empty_value_display = "BOŞ"


@admin.register(Favoriler)
class FavorilerAdmin(admin.ModelAdmin):
    list_display = ('kullanici', 'satilik_ilan', 'eklenme_tarihi')
    list_filter = ('kullanici',)
    search_fields = ('kullanici__username', 'satilik_ilan__ilanNo')

# Manuel olarak admin sitesine ekleme

# @admin.register(satilikResim)
# class satilikResimAdmin(admin.ModelAdmin):
#     list_display = ("ilan", "id")