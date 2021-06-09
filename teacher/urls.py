from django.urls import path
from .views import TeacherHomeView, TeacherProfileView, TeacherBaholashView


app_name = 'teacher'
urlpatterns = [
    path('home/', TeacherHomeView.as_view(), name='home'),
    path('profile/', TeacherProfileView.as_view(), name='profile'),
    path('baholash/', TeacherBaholashView.as_view(), name='baholash')
]