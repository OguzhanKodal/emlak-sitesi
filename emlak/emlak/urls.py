"""
URL configuration for emlak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anasayfa', views.anasayfa , name = 'anasayfa'),
]
"""
from django.contrib import admin
from django.urls import path,include
from . import views # views dosyasını import ediyoruz
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.anasayfa, name = 'anasayfa'), # anasayfa fonksiyonunu çağırıyoruz
    path('kiralikevler/',include('kiralikdaireler.urls')),
    path('satilikevler/',include('satilikdaireler.urls')),
    path('kurlar/', include('kurlar.urls')),
    path('anasayfa',views.anasayfa),
    path('admin/', admin.site.urls),
    path('login',views.user_login),
    path('register',views.user_register),
    path('logout',views.user_logout),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
