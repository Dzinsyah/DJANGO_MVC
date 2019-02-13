from django.shortcuts import render
def author(request):
    return render(request, 'author/author.html',{})
# Create your views here.
