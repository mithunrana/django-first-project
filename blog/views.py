from django.shortcuts import render
from index.models import  Person

def blog(request):
    return render(request,'blog.html')

def blogview(request,slug):
    SinglePerson =  Person.objects.get(first_name=slug)
    context = {
        'SinglePerson':SinglePerson
    }
    return render(request,'blogview.html',context)