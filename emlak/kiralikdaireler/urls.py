
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.kiralik_listesi), 
    path('knewilan',views.knewilan),  
    path('kevDetay/<int:ilanNo>/', views.kevDetay), 
    path('kduzenle/<int:ilanNo>/', views.kevDuzenle),
    path('kdetayEkle/<int:ilanNo>/', views.kdetayEkle),
    path('kfavori/ekle/<int:ilan_id>/', views.kfavori_ekle, name='kfavori_ekle'),
    path('kfavori/listesi/', views.kfavori_listesi, name='kfavori_listesi'),  
    path('kiralikevler/ev/<int:ilanNo>/', views.kevDetay, name='kevDetay'),
    path('ksearch/', views.ksearch, name='ksearch'),
    path('kevDetay/<int:ilan_id>/', views.kilan_detay, name='kevDetay')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

