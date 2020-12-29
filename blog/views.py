from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Blog


def all_blogs(request):
    # blogs = Blog.objects.all()  # grab all objects from Blog model
    # grab all objects in order of date and get first 5 model
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
