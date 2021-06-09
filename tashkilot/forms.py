from django import forms
from .models import Guruhlar, Tashkilot, Oqituvchi, Oquvchi
from main.models import Sohalar


class TashkilotRegistrationForm(forms.ModelForm):
    class Meta:
        model = Tashkilot
        fields = ('__all__')
        widgets = {
            'password': forms.PasswordInput,
            'ochilgan_yili': forms.DateTimeInput
        }


class AddGuruhForm(forms.ModelForm):
    class Meta:
        model = Guruhlar
        fields = ('__all__')


class AddFanForm(forms.ModelForm):
    class Meta:
        model = Sohalar # fanlar
        fields = ('__all__')


class AddOqituvchiForm(forms.ModelForm):
    class Meta:
        model = Oqituvchi
        fields = ('__all__')


class AddOquvchiForm(forms.ModelForm):
    class Meta:
        model = Oquvchi
        fields = ('__all__')