# Generated by Django 5.0.3 on 2024-05-20 08:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='kiralikTakip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilanNo', models.IntegerField(null=True)),
                ('il', models.CharField(max_length=20)),
                ('ilce', models.CharField(max_length=20)),
                ('mahalle', models.CharField(max_length=20)),
                ('sokak', models.CharField(max_length=20)),
                ('apartman', models.CharField(max_length=20)),
                ('apartmanNo', models.IntegerField(null=True)),
                ('fiyat', models.IntegerField(null=True)),
                ('m2', models.IntegerField(null=True)),
                ('aktiflik', models.BooleanField(null=True)),
                ('odaSayi', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='kiralikResim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(upload_to='kiralik_images/')),
                ('ilan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resimler', to='kiralikdaireler.kiraliktakip')),
            ],
        ),
        migrations.CreateModel(
            name='kiralikDetay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('binaYas', models.IntegerField(null=True)),
                ('katSayi', models.IntegerField(null=True)),
                ('kat', models.IntegerField(null=True)),
                ('isitma', models.CharField(max_length=20)),
                ('ilanTarih', models.DateField(null=True)),
                ('tapuDurum', models.CharField(max_length=20)),
                ('esya', models.CharField(max_length=20)),
                ('asonsor', models.CharField(max_length=20)),
                ('balkon', models.CharField(max_length=20)),
                ('otopark', models.CharField(max_length=20)),
                ('aidat', models.IntegerField(null=True)),
                ('aciklama', models.TextField(null=True)),
                ('kullanici', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kullanici', to='kiralikdaireler.kiraliktakip')),
            ],
        ),
        migrations.CreateModel(
            name='kFavoriler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eklenme_tarihi', models.DateTimeField(auto_now_add=True)),
                ('kullanici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kiralik_kullanici_favori', to=settings.AUTH_USER_MODEL)),
                ('kiralik_ilan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kiralik_favori_ilan', to='kiralikdaireler.kiraliktakip')),
            ],
            options={
                'unique_together': {('kullanici', 'kiralik_ilan')},
            },
        ),
    ]
