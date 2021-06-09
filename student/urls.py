from django.urls import path
from student.views import StudentProfileView, StudentHomeworkView, StudentFanView

app_name = 'student'
urlpatterns = [
    path('profile/', StudentProfileView.as_view(), name='profile'),
    path('homework/', StudentHomeworkView.as_view(), name='homework'),
    path('fan/', StudentFanView.as_view(), name='fan')
]