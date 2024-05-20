
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.satilik_listesi), 
    path('newilan',views.newilan),  
    path('evDetay/<int:ilanNo>/', views.evDetay), 
    path('duzenle/<int:ilanNo>/', views.evDuzenle),
    path('detayEkle/<int:ilanNo>/', views.detayEkle),
    path('favori/ekle/<int:ilan_id>/', views.favori_ekle, name='favori_ekle'),
    path('favori/listesi/', views.favori_listesi, name='favori_listesi'),  
    path('satilikevler/ev/<int:ilanNo>/', views.evDetay, name='evDetay'),
    path('search/', views.search, name='search'),
    path('evDetay/<int:ilan_id>/', views.ilan_detay, name='evDetay')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

