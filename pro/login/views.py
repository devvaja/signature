from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        r = User.objects.create_user(username=username,email=email,password=password)
        r.save()
        return redirect('/register/')
    return render(request,'register.html')

def Login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Check Username or Password')
            return redirect('/register/')

    return render(request,'register.html')

def index(request):
    return render(request,'index.html')