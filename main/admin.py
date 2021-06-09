from django.contrib import admin
from .models import TashkilotTurlari, Sohalar


class TashkilotTurlariAdmin(admin.ModelAdmin):
    class Meta:
        model = TashkilotTurlari
        fields = ['__all__']

admin.site.register(TashkilotTurlari, TashkilotTurlariAdmin)


class SohalarAdmin(admin.ModelAdmin):
    class Meta:
        model = Sohalar
        fields = ['__all__']

admin.site.register(Sohalar, SohalarAdmin)