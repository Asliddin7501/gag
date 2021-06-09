from django.db import models


# Tashkilot turlari (type)
class TashkilotTurlari(models.Model):
    tur = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tashkilot turi'
        verbose_name_plural = 'Tashkilot turlari'

    def __str__(self):
        return self.tur


# Fan va mutaxassislik
class Sohalar(models.Model):
    asosiy_soha = models.ForeignKey('Sohalar', on_delete=models.RESTRICT, null=True, default=None, blank=True) # Dasturlash
    soha = models.CharField(max_length=100) # Python, Java

    class Meta:
        verbose_name = 'Soha'
        verbose_name_plural = 'Sohalar'

    def __str__(self):
        return self.soha