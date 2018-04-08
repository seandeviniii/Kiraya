from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'Kiraya/hello.html',{})

def categories(request):
    return render(request,'Kiraya/categories.html',{})

def offers(request):
    return render(request,'Kiraya/offers.html',{})
