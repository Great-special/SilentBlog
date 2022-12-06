from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .forms import *

# Create your views here.


def home(request):
    context = {'blogs': BlogModel.objects.all()}
    return render(request, 'home.html', context)


def login_user(request):
    # form = LoginForm()
    message = ''
    if request.method == "POST":
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')
        
        user = authenticate(
                username=username,
                password=password,
            )
        
        if user is not None:
            print(user)
            login(request, user)
            message = f'Hello {user.username}! You have been logged in'
            return redirect('home')
        else:
            message = 'Login failed!'
        
        # form = LoginForm(request.POST)
        # if form.is_valid():
        #     user = authenticate(
        #         username=form.cleaned_data['username'],
        #         password=form.cleaned_data['password'],
        #     )
            # if user is not None:
            #     login(request, user)
            #     message = f'Hello {user.username}! You have been logged in'
            # else:
            #     message = 'Login failed!'
    return render(request, 'login.html',  context={'message': message})


def register(request):
    if request.method == "POST":
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'message': 'Username already exists'})
        else:
            User.objects.create_user(username=username, password=password)
            return redirect('login')
    return render(request, 'register.html')

@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login')
def add_blog(request):
 
    if request.method == 'POST' : # and request.FILES['image']
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_obj = form.save(commit=False)
            blog_obj.user = request.user
            # blog_obj.content = content
            blog_obj.save()
            
        return redirect('see_blog') 
        
    else:
        form = BlogForm()
 
    context = {'form': form}
    return render(request, 'add_blog.html', context)

@login_required(login_url='/login')
def blog_update(request, slug):
    context = {}

    blog_obj = BlogModel.objects.get(slug=slug)

    if blog_obj.user != request.user:
        return redirect('/')

    initial_dict = blog_obj
    form = BlogForm(instance=blog_obj)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog_obj)
   
        if form.is_valid():
            blog_obj = form.save(commit=False)
            blog_obj.user = request.user
            blog_obj.save()

            return redirect('see_blog')
        
    context['blog_obj'] = blog_obj
    context['form'] = form


    return render(request, 'update_blog.html', context)


def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = get_object_or_404(BlogModel, slug=slug)
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

@login_required(login_url='/login')
def see_blog(request):
    context = {}

    try:
        blog_objs = BlogModel.objects.filter(user=request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'see_blog.html', context)


@login_required(login_url='/login')
def blog_delete(request, slug):
    blog_obj = BlogModel.objects.get(slug=slug)
    print(blog_obj)

    if blog_obj.user == request.user:
        blog_obj.delete()

    return redirect('/see-blog/')

