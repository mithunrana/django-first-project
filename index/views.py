from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .models import  Slider
def home(request):
    PersonList = Person.objects.all()
    SliderList = Slider.objects.all()
    context={
        'Slider':SliderList,
        'Person':PersonList
    }
    return render(request,'index.html',context)

def about(request):
    return  HttpResponse("this is our abut page")


def contactus(request):
    return  HttpResponse("this is our contactus page")