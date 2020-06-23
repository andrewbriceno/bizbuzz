from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# from .models import Register

def index(request):
    return render(request,'bizzbuzz/index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'bizzbuzz/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:    #gets username and password, logs the user in
            login(user)
            #FIXME: redirect to index.html but logged in?  Show username in upper navbar
            #FIXME: IntegrityError at /bizzbuzz/signup/ UNIQUE constraint failed: auth_user.username
        else:
            # FIXME: user didn't put in the required fields or some other error occurred
            # needs to print something like "Sorry, login didn't work.  Try again!" on login page
            return render(request, 'bizzbuzz/login.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'bizzbuzz/signup.html')
    elif request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            #gets the fields from the form in signup.html and puts into database
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.create_user(username, None, password)
            #user.save()

            #run 'SELECT * from auth_user' in query console to see contents of this table
            return render(request, 'bizzbuzz/login.html')
    else:
        #FIXME: user didn't put in the required fields or some other error occurred
        #needs to print something like "Sorry, sign up didn't work.  Try again!" on signup page
        return render(request, 'bizzbuzz/signup.html')

# def forgotpassword(request):
#     return render(request,'bizzbuzz/forgotpassword.html')

def searchchannel(request):
    return render(request,'bizzbuzz/searchchannel.html')

#FIXME: shouldn't be able to hit this unless logged in
def home(request):
    return render(request,'bizzbuzz/home.html')

