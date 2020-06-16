from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):

    return render(request,'bizzbuzz/index.html')

def about(request):
    return render(request,'bizzbuzz/about.html')