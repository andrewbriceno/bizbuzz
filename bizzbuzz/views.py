from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):

    return render(request,'bizzbuzz/index.html')

def login(request):
    return render(request,'bizzbuzz/login.html')

def signup(request):
    return render(request,'bizzbuzz/signup.html')

def forgotpassword(request):
    return render(request,'bizzbuzz/forgotpassword.html')

def searchchannel(request):
    return render(request,'bizzbuzz/searchchannel.html')

