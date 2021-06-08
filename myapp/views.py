from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def myform(request):
    return render(request, 'myform.html')

def process(request):
    print("Welcome")
    print(request.method)
    print(request.POST)
    a = int(request.POST['txt1'])
    b = int(request.POST['txt2'])

    c = a + b
    print(c)

    return render(request, 'result.html', {'result': c})


class StudentList(ListView):
    model = Student
    template_name = 'stud_list.html'

