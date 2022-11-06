from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.forms import ModelForm


class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim

class Urun(models.Model):
    olusturan = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    isim = models.CharField(max_length=100, verbose_name='Urun ismi')
    resim = models.FileField(upload_to='urunler/', verbose_name='Urun resmi')
    aciklama = models.TextField(max_length=500, null=True)
    fiyat = models.IntegerField(null=True)

    def __str__(self):
        return self.isim



class Ucuz(models.Model):
    isim = models.CharField(max_length=100, verbose_name='İndirim ismi')
    resim = models.FileField(upload_to='indirimler/', verbose_name='indirim resmi')
    aciklama = models.TextField(max_length=500, null=True)
    indirim = models.IntegerField(null=True)

    def __str__(self):
        return self.isim


