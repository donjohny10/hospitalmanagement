from django.shortcuts import render
from .models import Department,Doctors

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):

    return render(request,'about.html')

def booking(request):
    numb={
        'list':[10,20,30,40,50,60,70],
    }
    return render(request,'booking.html',numb)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,'department.html',dict_dept)

def doctors(request):
    dict_doc={
        'doc_name':Doctors.objects.all()
    }
    
    return render(request,'doctors.html',dict_doc)

