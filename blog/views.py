from django.shortcuts import render
from blog.models import Comment

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'blog/index.html', {'blog': index})


def post(request):
    return render(request, 'blog/post.html', {})


def author(request):
    return render(request, 'blog/author.html', {})


def createPost(request):
    return render(request, 'blog/create_post.html', {})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')

        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, "login.html")
    return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'index.html')
    return render(request, "login.html")


def logout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/login')

def createComment(request):
    return render(request, 'blog/create_comment.html', {})
   
def postList(request):
    return render(request, 'blog/post_list.html', {})

