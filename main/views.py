from django.shortcuts import render
from django.views.generic import TemplateView


class MainIndex(TemplateView):
    template_name = 'main/index.html'

class TeacherProfile(TemplateView):
    template_name = 'main/profile.html'

class ChatBaholash(TemplateView):
    template_name = 'main/chat-baholash.html'