from django.shortcuts import render
from .models import Mentor

def mentor(request):
    add_post = Mentor.objects.all()
    return render(request, 'mentor/mentor.html',{'mentor':add_post})



# Create your views here.
