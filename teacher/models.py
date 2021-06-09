from django.db import models


class Mavzu(models.Model):
    oqituvchi = models.ForeignKey('tashkilot.Oqituvchi', on_delete=models.RESTRICT)
    guruh = models.ForeignKey('tashkilot.Guruhlar', on_delete=models.RESTRICT)
    mavzu_matni = models.TextField()
    mavzu_sanasi = models.DateTimeField()
    mavzu_fayli = models.FileField(upload_to='uyga-vazifa-fayllar/', default=None, null=True, blank=True)


class UygaVazifa(models.Model):
    oqituvchi = models.ForeignKey('tashkilot.Oqituvchi', on_delete=models.RESTRICT)
    guruh = models.ForeignKey('tashkilot.Guruhlar', on_delete=models.RESTRICT)
    oxirgi_muddat = models.DateTimeField()
    vazifa_matni = models.TextField(default=None, null=True, blank=True)
    vazifa_oyi = models.CharField(max_length=20)
    vazifa_kuni = models.IntegerField()
    muddat_oyi = models.CharField(max_length=20)
    muddat_kuni = models.IntegerField()
    vazifa_fayli = models.FileField(upload_to='uyga-vazifa-fayllar/', default=None, null=True, blank=True)


class Baholar(models.Model):
    oqituvchi = models.ForeignKey('tashkilot.Oqituvchi', on_delete=models.RESTRICT)
    oquvchi = models.ForeignKey('tashkilot.Oquvchi', on_delete=models.RESTRICT)
    fan = models.ForeignKey('main.Sohalar', on_delete=models.RESTRICT)
    javob = models.ForeignKey('student.Javob', on_delete=models.RESTRICT)
    baho = models.IntegerField()