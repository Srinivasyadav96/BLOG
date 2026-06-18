from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import Category_Form, BlogPostForm, AddUserForm, EditUserForm   
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


def generate_unique_slug(title):
    base_slug = slugify(title)
    slug = base_slug
    counter = 1
    while Blog.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug


# Create your views here.

@login_required(login_url='login')
def dashboards(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        'category_count': category_count,
        'blogs_count' : blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

#Category Functions
def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = Category_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = Category_Form()
    context={
        'form':form,
    }
    return render(request, 'dashboard/add_category.html', context)


def edit_category(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = Category_Form(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = Category_Form(instance=category)

    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')



#Posts Functions
def posts(request):
    posts=Blog.objects.all()
    context={
        'posts': posts
    }
    return render(request, 'dashboard/posts.html', context)

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)  # for files like images
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            title = form.cleaned_data['title']
            post.slug = generate_unique_slug(title)
            post.save()
            return redirect('posts')
    form = BlogPostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_post.html', context)


def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post) # instance means existing data
        if form.is_valid():
            post = form.save()
            title= form.cleaned_data['title']
            post.slug= slugify(title) + '-'+str(post.id) # making slug unique
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context={
        'form':form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html',context)


def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')


# User Functionalities
def users(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'dashboard/users.html', context)


def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = AddUserForm()
    context = {
        'form':form,
    }
    return render(request, 'dashboard/add_user.html', context)


def edit_user(request,pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    context = {
        'form':form,
    }
    return render(request, 'dashboard/edit_user.html', context)


def delete_user(request, pk):
    user= get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')