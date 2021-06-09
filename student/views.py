from django.shortcuts import render
from django.views.generic import View


class StudentProfileView(View):
    def get(self, request):
        return render(request, 'student/profile.html')
    def post(self, request):
        pass


class StudentHomeworkView(View):
    def get(self, request):
        return render(request, 'student/homework.html')
    def post(self, request):
        pass


class StudentFanView(View):
    def get(self, request):
        return render(request, 'student/fan.html')
    def post(self, request):
        pass