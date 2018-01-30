from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.students, name='home-student'),
    url(r'^([0-9]+)/$', views.student_folder, name='student-detail'),
]
