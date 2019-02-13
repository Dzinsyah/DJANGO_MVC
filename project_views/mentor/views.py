from django.shortcuts import render

def mentor(request):
    return render(request, 'mentor/mentor.html',{})

# Create your views here.
