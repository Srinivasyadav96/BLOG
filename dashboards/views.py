from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import Category_Form
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