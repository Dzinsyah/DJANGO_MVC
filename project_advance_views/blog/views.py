from django.shortcuts import render, redirect
from .models import Blog
from .form import Blog_form


def blog(request):
    add_post = Blog.objects.all()
    return render(request, 'blog/blog.html',{'isiblog':add_post})

def input_blog(request):
    if(request.method == 'POST'):
        form = Blog_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')

    else:
        form = Blog_form()
    return render(request, 'blog/input_blog.html', {'form':form})
        
# Create your views here.

