from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
def home(request):
    PersonList = Person.objects.all()
    context={
        'Person':PersonList
    }
    return render(request,'index.html',context)

def about(request):
    return  HttpResponse("this is our abut page")


def contactus(request):
    return  HttpResponse("this is our contactus page")