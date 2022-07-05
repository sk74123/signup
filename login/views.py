import imp
from os import uname
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'index.html')

def signup(request): 

    if request.method== 'POST' :

        username = request.POST['uname']
        fname= request.POST['fname']
        fname = fname.capitalize()
        lname= request.POST['lname']
        email= request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)

        myuser.first_name= fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, 'Account has been succesfully created')

        return redirect('signin')

        

    return render(request, 'signup.html')


def signin(request):

    if request.method == 'POST':

        uname= request.POST['uname']
        pass1 = request.POST['pass1']

        myuser = authenticate(username=uname, password= pass1)

        if request is not None:
            login(request, myuser)
            return redirect('home')

            messages.success(request, 'Successfully logged in')
        else:
            return redirect('signup')



    return render(request, 'signin.html')

def signout(request):
    logout(request)

    return redirect('signin')