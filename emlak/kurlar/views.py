import requests
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Kur

def kurlar_list(request):
    if request.method == 'POST':
        # Eski verileri sil
        Kur.objects.all().delete()

        currencies = {
            'USD': 'Dolar',
            'EUR': 'Euro',
            'GBP': 'Pound',
        }

        for currency, name in currencies.items():
            url = f'https://api.frankfurter.app/latest?from={currency}&to=TRY'
            response = requests.get(url)
            data = response.json()
            print(f"API Yanıtı {currency}:", data)  # API yanıtını yazdır

            if 'rates' in data and 'TRY' in data['rates']:
                try:
                    kur = Kur.objects.create(
                        ad=name,
                        tarih=datetime.strptime(data['date'], '%Y-%m-%d').date(),
                        deger=data['rates']['TRY']
                    )
                    print(f"Veritabanına Eklendi ({currency}):", kur)
                except Exception as e:
                    print(f"Veritabanı Hatası ({currency}):", e)

        return redirect('kurlar_list')

    kurlar = Kur.objects.all()
    return render(request, 'kurlar_list.html', {'kurlar': kurlar})
