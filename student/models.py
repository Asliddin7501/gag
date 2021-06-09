from django.db import models


class Javob(models.Model):
    uyga_vazifa = models.ForeignKey('teacher.UygaVazifa', on_delete=models.RESTRICT)
    oquvchi = models.ForeignKey('tashkilot.Oquvchi', on_delete=models.RESTRICT)
    javob_kuni = models.DateTimeField(auto_now_add=True)
    javob_matni = models.TextField(default=None, null=True, blank=True)
    javob_fayli = models.FileField(default=None, null=True, blank=True)