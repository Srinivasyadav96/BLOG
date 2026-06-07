from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category

# Create your views here.

def posts_by_category(request, category_id):
    #Fetch the posts that belongs to category with category_id
    posts = Blog.objects.filter(status='Published', category= category_id).order_by('-updated_at')
    try:
        category=Category.objects.get(id=category_id)
    except:
        #redirect the user to home page if category with category_id does not exits
        return redirect('home')
    #category = get_object_or_404(Category, pk=category_id)
    context={
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status= 'Published')
    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)