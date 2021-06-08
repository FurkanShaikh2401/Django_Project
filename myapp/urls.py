from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('myform/', views.myform, name='myform'),
    path('process/', views.process, name='process'),

    path('stud_list/', views.StudentList.as_view(), name='stud_list'),
]

