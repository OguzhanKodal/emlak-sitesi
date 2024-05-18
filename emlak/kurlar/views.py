import requests
from django.shortcuts import render
from datetime import datetime
from .models import Kur

def kurlar_list(request):
    currencies = {
        'USD': 'Dolar',
        'EUR': 'Euro',
        'GBP': 'Pound',
        'SAR': 'Riyal'
    }

    for currency, name in currencies.items():
        url = f'https://api.frankfurter.app/latest?from={currency}&to=TRY'
        response = requests.get(url)
        data = response.json()

        print(f"API Yanıtı {currency}:", data)

        if 'rates' in data and 'TRY' in data['rates']:
            try:
                Kur.objects.update_or_create(
                    ad=name,
                    tarih=datetime.strptime(data['date'], '%Y-%m-%d').date(),
                    defaults={'deger': data['rates']['TRY']}
                )
            except Exception as e:
                print(f"Veritabanı Hatası ({currency}):", e)

    kurlar = Kur.objects.all()
    print("Veritabanı Kayıtları:", kurlar)

    return render(request, 'kurlar_list.html', {'kurlar': kurlar})
