from django.urls import path
from .views import TashkilotRegistrationView, AddGuruhView, AddOqituvchiView, AddOquvchiView, TashkilotdashboardView, \
    AddFanView

app_name = 'tashkilot'
urlpatterns = [
    path('dashboard/', TashkilotdashboardView.as_view(), name='dashboard'),
    path('registration/', TashkilotRegistrationView.as_view(), name='registration'),
    path('guruh/add/', AddGuruhView.as_view(), name='add-guruh'),
    path('fan/add/', AddFanView.as_view(), name='add-fan'),
    path('oqituvchi/add/', AddOqituvchiView.as_view(), name='add-oqituvchi'),
    path('oquvchi/add/', AddOquvchiView.as_view(), name='add-oquvchi')
]