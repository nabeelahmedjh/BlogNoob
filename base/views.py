from multiprocessing import AuthenticationError, context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, Profile, Topic

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BlogForm, ProfileForm
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    if q != '':
        topic = Topic.objects.filter(name=q)
        print(topic)
        blogs = Blog.objects.filter(topic=topic[0:1])
    else:
        blog = blogs = Blog.objects.filter()

    context = {
        'blogs' : blogs
    }
    return render(request, 'base/home.html', context)


def blog(request, pk):

    blog = Blog.objects.get(id=pk)

    context = {'blog': blog}
    return render(request, 'base/blog.html', context)




@login_required(login_url='login')
def publishBlog(request):
    
    topics = Topic.objects.filter()
    if request.method == "POST":
        try:
            topic_name = request.POST.get('topic')

            topic, created = Topic.objects.get_or_create(name=topic_name)

            Blog.objects.create(
            title=request.POST.get('title'),
            author=request.user,
            topic=topic,
            body=request.POST.get('body')
            )

            messages.success(request,"Blog uploaded sucessfully")
            return redirect('home')
        except Exception as e:
            print(e)
            messages.error(request, "Something went wrong")
            return redirect('publish-blog')
        
    context = {
        "topics" : topics
    }

    return render(request, 'base/publish_blog.html', context)


@login_required(login_url='login')
def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)

        if form.is_valid():
            blog = form.save()
            return redirect('home')

    context = {
        'page': 'Update Blog',
        'form': form
    }

    return render(request, 'base/update.html', context)

@login_required(login_url='login')
def deleteBlog(request, pk):

    blog = Blog.objects.get(id=pk)

    if request.method == 'POST':
        if request.user == blog.author:
            blog.delete()
            messages.success(request, "Blog deleted sucessfully")
        else:
            messages.error(request, "You are not allowed to delete Blog")
        return redirect('home')
    context = {
        'blog': blog
    }

    return render(request, 'base/delete.html', context)



def registerUser(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            Profile.objects.create(
                user=user,
                full_name=user.username
            )
            
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong')

    context = {
        'form': form
    }

    return render(request, 'base/register.html', context)

def loginUser(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password doesn't exist")

    return render(request, 'base/login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    blogs = Blog.objects.filter(author=user)
    context = {
        'user': user,
        'blogs': blogs
    }
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def editProfile(request, pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(user=user)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "Successfully updated the profile")
            return redirect('home')


    return render(request, 'base/edit_profile.html', {"form": form})
