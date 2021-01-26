from django.http import HttpResponse

def employee(request):
    return  HttpResponse("this is employee first method")

def profile(request):
    return  HttpResponse("Employee Profile")