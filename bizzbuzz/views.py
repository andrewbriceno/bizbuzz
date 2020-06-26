# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from bizzbuzz.models import Preferences
# from .models import Register


def index_view(request):
    return render(request,'bizzbuzz/index.html')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'bizzbuzz/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # if request.user.is_authenticated:
        #     messages.error(request, 'This account is already logged in')
        #     return render(request, 'bizzbuzz/login.html')

        if user:    #gets username and password, logs the user in
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
            return render(request, 'bizzbuzz/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'GET':
        return render(request, 'bizzbuzz/signup.html')
    elif request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            #gets the fields from the form in signup.html and puts into database
            username = request.POST.get('username')
            password = request.POST.get('password')
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username, None, password)
                user.save()

                preference = Preferences(username=username)
                preference.save()
                #run 'SELECT * from auth_user' in query console to see contents of this table
                return redirect('selectchannel')
            else:
                messages.error(request, 'Username is already taken')
                return render(request, 'bizzbuzz/signup.html')
        else:
            messages.error(request, 'Please enter a valid username and password')
            return render(request, 'bizzbuzz/signup.html')

def forgotpassword_view(request):
    return render(request,'bizzbuzz/forgotpassword.html')

def searchchannel_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'bizzbuzz/searchchannel.html', {'name': request.user.username})

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'bizzbuzz/home.html', {'name': request.user.username})

def selectchannel_view(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')
    if request.method == 'GET':
        return render(request,'bizzbuzz/selectchannel.html')
    elif request.method == 'POST':
        if "Microsoft" in request.GET:
            username = request.POST.get('username')

        # if request.POST.get('username'):
        # if request.POST.get('username'):
        # if request.POST.get('username'):
        # if request.POST.get('username'):
        return render(request, 'bizzbuzz/login.html')

