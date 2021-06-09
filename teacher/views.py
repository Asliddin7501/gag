from django.shortcuts import render
from django.views.generic import View


class TeacherHomeView(View):
    def get(self, request):
        return render(request, 'teacher/home.html')
    def post(self, request):
        pass


class TeacherProfileView(View):
    def get(self, request):
        return render(request, 'teacher/profile.html')
    def post(self, request):
        pass


class TeacherAddMavzuView(View):
    def get(self, request):
        return render(request, '')


class TeacherBaholashView(View):
    def get(self, request):
        return render(request, 'teacher/baholash.html')
    def post(self, request):
        pass