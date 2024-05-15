
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
    path('favori/listesi/', views.favori_listesi, name='favori_listesi'),  # Bu satırın olduğundan emin olun
    path('satilikevler/ev/<int:ilanNo>/', views.evDetay, name='evDetay'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

