from django.contrib import admin
from .models import Kur

@admin.register(Kur)
class KurAdmin(admin.ModelAdmin):
    list_display = ('ad', 'deger', 'tarih')
    search_fields = ('ad',)
    list_filter = ('tarih',)
