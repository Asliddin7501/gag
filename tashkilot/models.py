from django.db import models
from main.models import Sohalar


# Maktab, universitet, o'quv markaz, kollej, litsey
class Tashkilot(models.Model):
    turi = models.ForeignKey('main.TashkilotTurlari', on_delete=models.RESTRICT)
    sohalar = models.ManyToManyField(Sohalar)
    nomi = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # rasm = models.ManyToManyField(Rasmlar)
    joylashuvi = models.TextField(default=None, null=True, blank=True)
    ochilgan_yili = models.DateTimeField(default=None, null=True, blank=True)


class Guruhlar(models.Model):
    tashkilot = models.ForeignKey('Tashkilot', on_delete=models.RESTRICT)
    sohalar = models.ManyToManyField(Sohalar)
    nomeri = models.CharField(max_length=50)
    # rasm = models.ManyToManyField(Rasmlar)


class Oqituvchi(models.Model):
    tashkilot = models.ForeignKey('Tashkilot', on_delete=models.RESTRICT)
    fanlar = models.ManyToManyField(Sohalar)  # o'qitadigan fanlari
    guruhlari = models.ManyToManyField(Guruhlar)
    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=50)
    sharif = models.CharField(max_length=50)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    tugilgan_kun = models.DateTimeField()
    # rasm = models.ImageField(upload_to='oqituvchi/')
    ish_tajribasi = models.TextField(default=None, null=True, blank=True) # ishlagan joylari va yili


class Oquvchi(models.Model):
    tashkilot = models.ForeignKey('Tashkilot', on_delete=models.RESTRICT)
    guruhi = models.ForeignKey('Guruhlar', on_delete=models.RESTRICT)
    fanlar = models.ManyToManyField(Sohalar)  # o'qiydigan fanlari
    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=50)
    sharif = models.CharField(max_length=50)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    tugilgan_kun = models.DateTimeField()
    # rasm = models.ImageField(upload_to='oquvchi/')