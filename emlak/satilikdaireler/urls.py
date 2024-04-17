
from django.urls import path
from . import views

app_name = 'satilikdaireler'

urlpatterns = [
    path('', views.satilik_listesi, name='satilik_listesi'),
    path('newilan/', views.newilan, name='newilan'),  
    path('detay/<int:ilanNo>/', views.evDetay, name='evDetay'), 
    path('duzenle/<int:ilanNo>/', views.evDuzenle, name='duzenle'),
    path('ekle/<int:ilanNo>/', views.detayEkle, name='detayEkle'),

]

