from django.db import models

class Kur(models.Model):
    ad = models.CharField(max_length=100)
    deger = models.DecimalField(max_digits=10, decimal_places=4)
    tarih = models.DateField()

    def __str__(self):
        return f"{self.ad} - {self.deger}"
