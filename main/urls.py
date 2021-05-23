from django.urls import path
from .views import MainIndex, TeacherProfile, ChatBaholash

app_name = 'main'
urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('profile/', TeacherProfile.as_view(), name='teacher-profile'),
    path('chat-baholash/', ChatBaholash.as_view(), name='chat-baholash')
]