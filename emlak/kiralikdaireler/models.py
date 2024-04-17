from django.db import models

# Create your models here.


# Create your models here.

class ilan(models.Model):
  num=models.CharField(max_length=15)
  ad=models.CharField(max_length=15)
  soyad=models.CharField(max_length=15)
  ezber = models.CharField(max_length=255, default='VarsayilanDeger')