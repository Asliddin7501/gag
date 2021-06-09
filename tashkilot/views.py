from django.shortcuts import render
from django.views.generic import View
from .forms import TashkilotRegistrationForm, AddGuruhForm, AddOqituvchiForm, AddOquvchiForm, AddFanForm


class TashkilotdashboardView(View):
    def get(self, request):
        return render(request, 'tashkilot/dashboard.html')
    def post(self, request):
        pass


class TashkilotRegistrationView(View):
    def get(self, request):
        return render(request, 'tashkilot/forms.html', {
            'form': TashkilotRegistrationForm()
        })
    def post(self, request):
        pass


class AddGuruhView(View):
    def get(self, request):
        return render(request, 'tashkilot/forms.html', {
            'form': AddGuruhForm()
        })
    def post(self, request):
        pass


class AddFanView(View):
    def get(self, request):
        return render(request, 'tashkilot/forms.html', {
            'form': AddFanForm()
        })

    def post(self, request):
        pass


class AddOqituvchiView(View):
    def get(self, request):
        return render(request, 'tashkilot/forms.html', {
            'form': AddOqituvchiForm()
        })
    def post(self, request):
        pass


class AddOquvchiView(View):
    def get(self, request):
        return render(request, 'tashkilot/forms.html', {
            'form': AddOquvchiForm()
        })
    def post(self, request):
        pass