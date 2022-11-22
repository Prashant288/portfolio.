from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def portfolio(request):
    return render(request,"portfolio.html")

def contact(request):
    return render(request,"contact.html")

def project(request):
    return render(request,"project.html")