from django.shortcuts import render
from blog.models import Comment, Post
from django.views import generic
from django.shortcuts import get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required


def index(request):
    posts = Post.objects.filter()
    return render(request, 'blog/index.html', {'posts': posts})

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
    messages.success(request, "Successfully Logged Out")
    return redirect('/login')

def createComment(request):
    return render(request, 'blog/create_comment.html', {})

   
def postList(request):
    return render(request, 'blog/post_list.html', {})



class PostDetailView(generic.DetailView):
    model = Post

    def post_detail_view(request, primary_key):
        post = get_object_or_404(Post, pk=primary_key)
        return render(request, 'blog/post.html', context={'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.created_date = timezone.now()
            post.save()
            return render(request, 'blog/index.html',
                          {})
    else:
        form = postNew()

    return render(request, 'blog/create_post.html', {'form': form})

