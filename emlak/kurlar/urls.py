from django.urls import path
from . import views

urlpatterns = [
    path('', views.kurlar_list, name='kurlar_list'),
]
