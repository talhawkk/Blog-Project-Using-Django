from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    
    return render(request, 'blog/home.html',)

def aboutus(request):
    
    return render(request, 'blog/aboutus.html',)

def contactus(request):
    
    return render(request, 'blog/contactus.html',)

def dashboard(request):
    return render(request, 'blog/dashboard.html',)

def user_logout(request):
    logout(request)
    messages.success(request,'You have been Logged out Successfully')
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You have been Registered Successfully')
            # form=SignUpForm()
    else:
        form=SignUpForm()
    return render(request, 'blog/signup.html',{'form':form})

def user_login(request):
    # logout(request)
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request ,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user =authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'You have been Logged in Successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
                form=LoginForm()
        return render(request, 'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')