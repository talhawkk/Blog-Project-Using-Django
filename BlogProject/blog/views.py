from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post,Category
from django.contrib.auth.models import Group
# Create your views here.
def home(request):
    post=Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/home.html',{'posts':post,'categories':categories})

def aboutus(request):
    
    return render(request, 'blog/aboutus.html',)

def contactus(request):
    
    return render(request, 'blog/contactus.html',)

def dashboard(request):
    if request.user.is_authenticated:
        post=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()

        return render(request, 'blog/dashboard.html',{'posts':post,'full_name':full_name,'gps':gps})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    messages.success(request,'You have been Logged out Successfully!!')
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
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
                    messages.error(request,'Invalid Credentials')
                    return HttpResponseRedirect('/login/')
                    
        else:
                form=LoginForm()
        return render(request, 'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
    
def edit(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request,'Your changes has been updated')
                return HttpResponseRedirect('/dashboard')
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request,'blog/edit.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PostForm(request.POST)
            if form.is_valid():
                # form=form.cleaned_data()
                form.save()
                messages.success(request,'Your blog has been Published')
                return HttpResponseRedirect('/dashboard/')
        else:
            form=PostForm()
        return render(request, 'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
def delete(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            messages.success(request,'Your Blog has been Deleted')
            return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login/')
    
def readblog(request, id):
    pi=Post.objects.get(pk=id)
    blog=pi
    return render(request, 'blog/readblog.html',{'post':blog})


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/category_posts.html', {'posts': posts, 'category': category})
